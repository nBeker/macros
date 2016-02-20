"""
The following script records any keyboard action and mouse operation.
The output will be a Python file which can be executed and repeat the user input.

Idea Originating Credit: A.S.
"""
import argparse
import ctypes
import json
import os.path
from string import Template
from win32gui import GetCursorPos as mouse_position

import pythoncom
import pyHook
import win32con


actions_list = list()
MOUSE_EVENT = 0
KEYBOARD_EVENT = 1


def handle_arguments():
    def macros_file(path):
        basename = os.path.basename(path)
        if not basename.endswith(".py"):
            basename += ".py"
        return basename


    parser = argparse.ArgumentParser(prog="Macros Creator",
                                     description="Create macros for repeated use")
    parser.add_argument("macro_name", help="The macro name", type=macros_file)

    return parser.parse_args()


# MOUSE_EVENTS contains cross mapping between pyHook to WinAPI constants
MOUSE_EVENTS = {
    pyHook.HookConstants.WM_MBUTTONDOWN: win32con.MOUSEEVENTF_MIDDLEDOWN,
    pyHook.HookConstants.WM_MBUTTONUP: win32con.MOUSEEVENTF_MIDDLEUP,
    pyHook.HookConstants.WM_RBUTTONDOWN: win32con.MOUSEEVENTF_RIGHTDOWN,
    pyHook.HookConstants.WM_RBUTTONUP: win32con.MOUSEEVENTF_RIGHTUP,
    pyHook.HookConstants.WM_LBUTTONDOWN: win32con.MOUSEEVENTF_LEFTDOWN,
    pyHook.HookConstants.WM_LBUTTONUP: win32con.MOUSEEVENTF_LEFTUP
}


def OnMouseEvent(event):
    global actions_list
    # TODO: fix this - event.Position
    actions_list.append((MOUSE_EVENT, (MOUSE_EVENTS[event.Message], mouse_position())))

    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True


def OnKeyboardEvent(event):
    if event.KeyID is 35:
        ctypes.windll.user32.PostQuitMessage(0)
        return True

    global actions_list
    actions_list.append((KEYBOARD_EVENT, (event.KeyID, event.Message)))
    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True


if __name__ == "__main__":
    args = handle_arguments()

    # create the hook mananger
    hm = pyHook.HookManager()
    # register two callbacks
    hm.MouseAllButtons = OnMouseEvent
    hm.KeyAll = OnKeyboardEvent

    # hook into the mouse and keyboard events
    hm.HookMouse()
    hm.HookKeyboard()

    pythoncom.PumpMessages()

    if actions_list:
        # Saving the information:

        with open("template.py") as t:
            template = Template(t.read())

        with open(args.macro_name, 'w') as f:
            f.write(template.substitute(actions_json=json.dumps(actions_list)))

