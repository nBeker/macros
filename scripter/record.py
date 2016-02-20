import argparse
import ctypes
import json
import os.path

import pythoncom
import pyHook
from string import Template


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


def OnMouseEvent(event):
    global actions_list
    actions_list.append((MOUSE_EVENT, (event.Message, event.Position)))

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


# create the hook mananger
hm = pyHook.HookManager()
# register two callbacks
hm.MouseAllButtons = OnMouseEvent
hm.KeyAll = OnKeyboardEvent

# hook into the mouse and keyboard events
hm.HookMouse()
hm.HookKeyboard()

if __name__ == "__main__":
    args = handle_arguments()

    pythoncom.PumpMessages()

    if actions_list:
        # Saving the information:

        with open("template.py") as t:
            template =  Template(t.read())

        with open(args.macro_name, 'w') as f:
            f.write(template.substitute(actions_json=json.dumps(actions_list)))

