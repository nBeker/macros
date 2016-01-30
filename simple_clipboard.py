import win32clipboard


class simple_clipboard(object):
    def __init__(self):
        self._is_open = False

    def set(self, data):
        if self._is_open:
            win32clipboard.SetClipboardText(data, win32clipboard.CF_UNICODETEXT)
        else:
            raise RuntimeError("Clipboard not opened")

    def get(self):
        if self._is_open:
            return win32clipboard.GetClipboardData()
        else:
            raise RuntimeError("Clipboard not opened")

    def empty(self):
        if self._is_open:
            return win32clipboard.EmptyClipboard()
        else:
            raise RuntimeError("Clipboard not opened")

    def __enter__(self):
        if not self._is_open:
            win32clipboard.OpenClipboard()
            self._is_open = True
            return self

    def __exit__(self, type, value, traceback):
        if self._is_open:
            win32clipboard.CloseClipboard()
            self._is_open = False