from simple_clipboard import simple_clipboard

import virtual_keyboard


class UseKeyboard(object):
    send_alt_tab  = lambda x: virtual_keyboard.press_combo("A\t")
    send_mark_all = lambda x: virtual_keyboard.press_combo("^a")
    send_paste    = lambda x: virtual_keyboard.press_combo("^v")
    send_copy     = lambda x: virtual_keyboard.press_combo("^c")
    send_cut      = lambda x: virtual_keyboard.press_combo("^x")

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
    The manipulator function cuts all text from the previously focused window(last foreground window before script call)
    and then performs a manipulation on the text with a given function. after the manipulation the text will be returned
    On case of failure, the text will be returned also.
    :param function: the manipulation function
    :param replace_source: replace the source text if it can
    :param empty_clipboard: empty clipboard in-order to clean it
    """
    try:
        with simple_clipboard() as clipboard:
            data = clipboard.get()
            if empty_clipboard:
                clipboard.empty()

            clipboard.set(function(data))

    except Exception as e:
        print(e.args)
        input()


def manipulator_with_keyboard(function, empty_clipboard=False, replace_source=True, mark_all=False):
    """
    The manipulator function cuts all text from the previously focused window(last foreground window before script call)
    and then performs a manipulation on the text with a given function. after the manipulation the text will be returned
    On case of failure, the text will be returned also.
    :param function: the manipulation function
    :param replace_source: replace the source text if it can
    :param empty_clipboard: empty clipboard in-order to clean it
    """
    with UseKeyboard(replace_source=replace_source, mark_all=mark_all):
        manipulator(function=function, empty_clipboard=empty_clipboard)
