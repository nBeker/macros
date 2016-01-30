from simple_clipboard import simple_clipboard

import virtual_keyboard

send_alt_tab = lambda: virtual_keyboard.press_combo("A\t")
send_mark_all = lambda: virtual_keyboard.press_combo("^a")
send_paste = lambda: virtual_keyboard.press_combo("^v")
send_copy = lambda: virtual_keyboard.press_combo("^c")
send_cut = lambda: virtual_keyboard.press_combo("^x")

def manipulator(function, replace_source=True, empty_clipboard=False, mark_all=False):
    """
    The manipulator function cuts all text from the previously focused window(last foreground window before script call)
    and then performs a manipulation on the text with a given function. after the manipulation the text will be returned
    On case of failure, the text will be returned also.
    :param function: the manipulation function
    :param replace_source: replace the source text if it can
    :param empty_clipboard: empty clipboard in-order to clean it
    """
    try:
        # import ipdb; ipdb/set_trace()
        # Alt + Tab to return to the previous context
        send_alt_tab()
        if mark_all:
            send_mark_all()

        if replace_source:
            # Cut text
            send_cut()
        else:
            # Copy text
            send_copy()

        with simple_clipboard() as clipboard:
            data = clipboard.get()
            if empty_clipboard:
                clipboard.empty()
            clipboard.set(function(data))

    except Exception as e:
        # Alt + Tab to return to the python context
        send_alt_tab()
        print(e.args)
        input()
    finally:
        if replace_source:
            # Ctrl+V to Paste the new text
            send_paste()