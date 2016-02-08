"""
Wrapping the clipboard functions for it's text-only purposes.
Set, Get, Empty
will handle the open and closing of clipboard for each methods
"""

import win32clipboard


class clipboard(object):
    @staticmethod
    def set(data):
        with clipboard():
            win32clipboard.SetClipboardText(data, win32clipboard.CF_UNICODETEXT)

    @staticmethod
    def get():
        with clipboard():
            return win32clipboard.GetClipboardData()

    @staticmethod
    def empty():
        with clipboard():
            return win32clipboard.EmptyClipboard()

    def __enter__(self):
        win32clipboard.OpenClipboard()
        return self

    def __exit__(self, type, value, traceback):
        win32clipboard.CloseClipboard()
        self._is_open = False