from simple_clipboard import clipboard

import virtual_keyboard


class UseKeyboard(object):
    send_alt_tab = lambda x: virtual_keyboard.press_combo("A\t")
    send_mark_all = lambda x: virtual_keyboard.press_combo("^a")
    send_paste = lambda x: virtual_keyboard.press_combo("^v")
    send_copy = lambda x: virtual_keyboard.press_combo("^c")
    send_cut = lambda x: virtual_keyboard.press_combo("^x")

    def __init__(self, replace_source=True, mark_all=False):
        self._replace_source = replace_source
        self._mark_all = mark_all

    def __enter__(self):
        self.send_alt_tab()
        if self._mark_all:
            self.send_mark_all()

        if self._replace_source:
            # Cut text
            self.send_cut()
        else:
            # Copy text
            self.send_copy()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._replace_source:
            self.send_paste()


def manipulator(function, empty_clipboard=False):
    """
    Performs a manipulation using a given function the clipboard text
    :param function: The clipboard text manipulation function
    :param empty_clipboard: Clear the contents of the clipboard
    """
    try:
        data = clipboard.get()
        if empty_clipboard:
            clipboard.empty()

        clipboard.set(function(data))

    except Exception as e:
        input(e.args)


def manipulator_with_keyboard(function, empty_clipboard=False, replace_source=True, mark_all=False):
    """
    Using the clipboard manipulator but also sends Cut & Paste OR Copy keystrokes.
    Text from the previously focused window(last foreground window before script call) will be act upon.
    :param function: The clipboard text manipulation function
    :param empty_clipboard: Clear the contents of the clipboard
    :param replace_source: If True, will Cut the text and Paste upon completion. if False will only Copy to clipboard
                           and manipulate it. The result will be kept in the clipboard.
    :param mark_all: Whether to send a mark-all key combination (Ctrl+A)
    """
    with UseKeyboard(replace_source=replace_source, mark_all=mark_all):
        manipulator(function=function, empty_clipboard=empty_clipboard)
