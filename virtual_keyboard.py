from win32api import keybd_event as keyboard_event
from time import sleep

from win32con import KEYEVENTF_KEYUP as RELEASE_KEY
import win32con


SLEEP_CONST = .05

# Giant dictionary to hold key name and VK value
VK_CODE = {'BACKSPACE': win32con.VK_BACK,
           'TAB': win32con.VK_TAB,
           '\t': win32con.VK_TAB,
           'clear': win32con.VK_CLEAR,
           'ENTER': win32con.VK_RETURN,
           '\n': win32con.VK_RETURN,
           'SHIFT': win32con.VK_SHIFT,
           'S': win32con.VK_SHIFT,
           'CTRL': win32con.VK_CONTROL,
           '^': win32con.VK_CONTROL,
           'ALT': win32con.VK_MENU,
           'A': win32con.VK_MENU,
           'PAUSE': win32con.VK_PAUSE,
           'CAPSLOCK': win32con.VK_CAPITAL,
           'ESC': win32con.VK_ESCAPE,
           'SPACEBAR': win32con.VK_SPACE,
           ' ': win32con.VK_SPACE,
           'PAGE': win32con.VK_PRIOR,
           'PAGE_DOWN': win32con.VK_NEXT,
           'END': win32con.VK_END,
           'HOME': win32con.VK_HOME,
           'LEFT': win32con.VK_LEFT,
           'UP': win32con.VK_UP,
           'RIGHT': win32con.VK_RIGHT,
           'DOWN': win32con.VK_DOWN,
           'SELECT': win32con.VK_SELECT,
           'PRINT': win32con.VK_PRINT,
           'EXECUTE': win32con.VK_EXECUTE,
           'PRINT_SCREEN': win32con.VK_SNAPSHOT,
           'INS': win32con.VK_INSERT,
           'DEL': win32con.VK_DELETE,
           'HELP': win32con.VK_HELP,
           '0': 0x30,
           '1': 0x31,
           '2': 0x32,
           '3': 0x33,
           '4': 0x34,
           '5': 0x35,
           '6': 0x36,
           '7': 0x37,
           '8': 0x38,
           '9': 0x39,
           'a': 0x41,
           'b': 0x42,
           'c': 0x43,
           'd': 0x44,
           'e': 0x45,
           'f': 0x46,
           'g': 0x47,
           'h': 0x48,
           'i': 0x49,
           'j': 0x4A,
           'k': 0x4B,
           'l': 0x4C,
           'm': 0x4D,
           'n': 0x4E,
           'o': 0x4F,
           'p': 0x50,
           'q': 0x51,
           'r': 0x52,
           's': 0x53,
           't': 0x54,
           'u': 0x55,
           'v': 0x56,
           'w': 0x57,
           'x': 0x58,
           'y': 0x59,
           'z': 0x5A,
           'LWIN': win32con.VK_LWIN,
           'WIN': win32con.VK_LWIN,
           'WINKEY': win32con.VK_LWIN,
           'W': win32con.VK_LWIN,
           'RWIN': win32con.VK_RWIN,
           'NUMPAD_0': win32con.VK_NUMPAD0,
           'NUMPAD_1': win32con.VK_NUMPAD1,
           'NUMPAD_2': win32con.VK_NUMPAD2,
           'NUMPAD_3': win32con.VK_NUMPAD3,
           'NUMPAD_4': win32con.VK_NUMPAD4,
           'NUMPAD_5': win32con.VK_NUMPAD5,
           'NUMPAD_6': win32con.VK_NUMPAD6,
           'NUMPAD_7': win32con.VK_NUMPAD7,
           'NUMPAD_8': win32con.VK_NUMPAD8,
           'NUMPAD_9': win32con.VK_NUMPAD9,
           'MULTIPLY': win32con.VK_MULTIPLY,
           '*': win32con.VK_MULTIPLY,
           'ADD': win32con.VK_ADD,
           '+': win32con.VK_ADD,
           'SEPARATOR': win32con.VK_SEPARATOR,
           'SUBTRACT': win32con.VK_SUBTRACT,
           '-': win32con.VK_SUBTRACT,
           'DECIMAL': win32con.VK_DECIMAL,
           '.': win32con.VK_DECIMAL,
           'DIVIDE': win32con.VK_DIVIDE,
           '/': win32con.VK_DIVIDE,
           'F1': win32con.VK_F1,
           'F2': win32con.VK_F2,
           'F3': win32con.VK_F3,
           'F4': win32con.VK_F4,
           'F5': win32con.VK_F5,
           'F6': win32con.VK_F6,
           'F7': win32con.VK_F7,
           'F8': win32con.VK_F8,
           'F9': win32con.VK_F9,
           'F10': win32con.VK_F10,
           'F11': win32con.VK_F11,
           'F12': win32con.VK_F12,
           'F13': win32con.VK_F13,
           'F14': win32con.VK_F14,
           'F15': win32con.VK_F15,
           'F16': win32con.VK_F16,
           'F17': win32con.VK_F17,
           'F18': win32con.VK_F18,
           'F19': win32con.VK_F19,
           'F20': win32con.VK_F20,
           'F21': win32con.VK_F21,
           'F22': win32con.VK_F22,
           'F23': win32con.VK_F23,
           'F24': win32con.VK_F24,
           'NUM_LOCK': win32con.VK_NUMLOCK,
           'SCROLL_LOCK': win32con.VK_SCROLL,
           'LEFT_SHIFT': win32con.VK_LSHIFT,
           'RIGHT_SHIFT ': win32con.VK_RSHIFT,
           'LEFT_CONTROL': win32con.VK_LCONTROL,
           'RIGHT_CONTROL': win32con.VK_RCONTROL,
           'LEFT_MENU': win32con.VK_LMENU,
           'RIGHT_MENU': win32con.VK_RMENU,
           'BROWSER_BACK': win32con.VK_BROWSER_BACK,
           'BROWSER_FORWARD': win32con.VK_BROWSER_FORWARD,
           'BROWSER_REFRESH': 0XA8,
           'BROWSER_STOP': 0XA9,
           'BROWSER_SEARCH': 0XAA,
           'BROWSER_FAVORITES': 0XAB,
           'BROWSER_START_AND_HOME': 0XAC,
           'VOLUME_MUTE': win32con.VK_VOLUME_MUTE,
           'VOLUME_DOWN': win32con.VK_VOLUME_DOWN,
           'VOLUME_UP': win32con.VK_VOLUME_UP,
           'NEXT_TRACK': win32con.VK_MEDIA_NEXT_TRACK,
           'PREVIOUS_TRACK': win32con.VK_MEDIA_PREV_TRACK,
           'STOP_MEDIA': 0XB2,
           'TOGGLE_MEDIA': win32con.VK_MEDIA_PLAY_PAUSE,
           'START_MAIL': 0XB4,
           'SELECT_MEDIA': 0XB5,
           'START_APPLICATION_1': 0XB6,
           'START_APPLICATION_2': 0XB7,
           'ATTN_KEY': win32con.VK_ATTN,
           'CRSEL_KEY': win32con.VK_CRSEL,
           'EXSEL_KEY': win32con.VK_EXSEL,
           'PLAY_KEY': win32con.VK_PLAY,
           'ZOOM_KEY': win32con.VK_ZOOM,
           'CLEAR_KEY': win32con.VK_OEM_CLEAR,
           # '+': win32con.VK_OEM_PLUS,
           ',': 0xBC,
           # '-': 0xBD,
           # '.': 0xBE,
           # '/': 0xBF,
           '`': 0xC0,
           ';': 0xBA,
           '[': 0xDB,
           '\\': 0xDC,
           ']': 0xDD,
           "'": 0xDE}


def press(keys_list):
    """
    one press, one release.
    :param keys_list:  list of keys
    """
    for key in keys_list:
        keyboard_event(VK_CODE[key], 0, 0, 0)
        sleep(SLEEP_CONST)
        keyboard_event(VK_CODE[key], 0, RELEASE_KEY, 0)


def hold(keys_list):
    """
    press and hold. Do NOT release.
    :param keys_list: list of keys
    """
    for key in keys_list:
        keyboard_event(VK_CODE[key], 0, 0, 0)
        sleep(SLEEP_CONST)


def release(keys_list):
    """
    release depressed keys
    :param keys_list: list of keys
    """
    for key in keys_list:
        keyboard_event(VK_CODE[key], 0, RELEASE_KEY, 0)


def press_combo(keys_list):
    """
    Holds and then Releases a key_list
    :param keys_list: list of keys
    """
    hold(keys_list)
    release(keys_list)