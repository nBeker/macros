import win32clipboard as clipboard
import virtual_keyboard


def manipulator(function):
    """
    The manipulator function cuts all text from the previously focused window(last foreground window before script call)
    and then performs a manipulation on the text with a given function. after the manipulation the text will be returned
    On case of failure, the text will be returned also.
    :param function: the manipulation function
    """
    try:
        # Alt + Tab to return to the previous context
        virtual_keyboard.press_combo("A\t")
        # Ctrl+A+X to Cut all text
        virtual_keyboard.press_combo("^ax")

        clipboard.OpenClipboard()
        data = clipboard.GetClipboardData()
        clipboard.SetClipboardText(function(data), clipboard.CF_UNICODETEXT)

    except Exception as e:
        # Alt + Tab to return to the python context
        virtual_keyboard.press_combo("A\t")
        print(e.args)
        input()
    finally:
        clipboard.CloseClipboard()
        # Ctrl+V to Paste the new text
        virtual_keyboard.press_combo("^v")