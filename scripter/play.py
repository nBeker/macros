from win32api import keybd_event as keyboard_event
from win32api import mouse_event
from win32api import SetCursorPos as set_mouse_position
import json
from time import sleep

from win32con import KEYEVENTF_KEYUP as RELEASE_KEY
import pyHook


MOUSE_EVENT = 0
KEYBOARD_EVENT = 1


def MouseAction(action):
    """
    Performs mouse action.
    First, set mouse position at the required coordinate, and then operates.
    operations means either press or de-press any mouse key
    :param action: a tuple \ list contains the operation (key-press \ key-de-press) and cursor position
    :return:
    """
    operation, position = action
    set_mouse_position(position)
    mouse_event(operation, 0, 0, 0, 0)


def KeyboardAction(action):
    """
    Performs keyboard action (either press or de-press key)
    :param action: a tuple \ list contains the key_id and the operation (press \ de-press)
    :return:
    """
    key_id, operation = action
    if operation == pyHook.HookConstants.WM_KEYDOWN:
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
