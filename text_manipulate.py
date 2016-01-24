import win32clipboard as clipboard

import virtual_keyboard


def manipulator(function, replace_source=True, empty_clipboard=False):
    """
    The manipulator function cuts all text from the previously focused window(last foreground window before script call)
    and then performs a manipulation on the text with a given function. after the manipulation the text will be returned
    On case of failure, the text will be returned also.
    :param function: the manipulation function
    :param replace_source: replace the source text if it can
    :param empty_clipboard: empty clipboard in-order to clean it
    """
    try:
        # Alt + Tab to return to the previous context
        virtual_keyboard.press_combo("A\t")
        if replace_source:
            # Ctrl+A+X to Cut all text
            virtual_keyboard.press_combo("^ax")
        else:
            # Ctrl+A+C to Cut all text
            virtual_keyboard.press_combo("^ac")

        clipboard.OpenClipboard()
        data = clipboard.GetClipboardData()

        if empty_clipboard:
            clipboard.EmptyClipboard()

        clipboard.SetClipboardText(function(data), clipboard.CF_UNICODETEXT)

    except Exception as e:
        # Alt + Tab to return to the python context
        virtual_keyboard.press_combo("A\t")
        print(e.args)
        input()
    finally:
        clipboard.CloseClipboard()
        if replace_source:
            # Ctrl+V to Paste the new text
            virtual_keyboard.press_combo("^v")