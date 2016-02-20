from win32api import keybd_event as keyboard_event
from win32api import mouse_event
from win32api import SetCursorPos as set_mouse_position
import json
from time import sleep

from win32con import KEYEVENTF_KEYUP as RELEASE_KEY
import win32con
from pyHook import HookConstants as pyhook_consts


MOUSE_EVENT = 0
KEYBOARD_EVENT = 1

MOUSE_EVENTS = {
    pyhook_consts.WM_MBUTTONDOWN: win32con.MOUSEEVENTF_MIDDLEDOWN,
    pyhook_consts.WM_MBUTTONUP: win32con.MOUSEEVENTF_MIDDLEUP,
    pyhook_consts.WM_RBUTTONDOWN: win32con.MOUSEEVENTF_RIGHTDOWN,
    pyhook_consts.WM_RBUTTONUP: win32con.MOUSEEVENTF_RIGHTUP,
    pyhook_consts.WM_LBUTTONDOWN: win32con.MOUSEEVENTF_LEFTDOWN,
    pyhook_consts.WM_LBUTTONUP: win32con.MOUSEEVENTF_LEFTUP
}
# win32con.MOUSEEVENTF_ABSOLUTE   
# win32con.MOUSEEVENTF_XDOWN
# win32con.MOUSEEVENTF_XUP
# win32con.MOUSEEVENTF_MOVE       
# win32con.MOUSEEVENTF_WHEEL

def MouseAction(action):
    operation, position = action
    set_mouse_position(position)
    print(operation, pyhook_consts.MsgToName(operation))
    print(position)
    mouse_event(MOUSE_EVENTS.get(operation), 0, 0, 0, 0)


def KeyboardAction(action):
    key_id, operation = action
    if operation == pyhook_consts.WM_KEYDOWN:
        keyboard_event(key_id, 0, 0, 0)
    else:
        keyboard_event(key_id, 0, RELEASE_KEY, 0)


actions = {MOUSE_EVENT: MouseAction,
           KEYBOARD_EVENT: KeyboardAction}


def play_macro(macro_json, action_delay=.1, repeats=1, animate_mouse=False):
    # Loading the macro
    actions_list = json.loads(macro_json)
    for i in range(repeats):
        for action in actions_list:
            actions[action[0]](action[1])
            sleep(action_delay)
