from win32api import keybd_event as keyboard_event
from time import sleep

from win32con import KEYEVENTF_KEYUP as RELEASE_KEY


SLEEP_CONST = .05

# Giant dictionary to hold key name and VK value
VK_CODE = {'BACKSPACE': 0x08,
           'TAB': 0x09,
           '\t': 0x09,
           'clear': 0x0C,
           'ENTER': 0x0D,
           '\n': 0x0D,
           'SHIFT': 0x10,
           'S': 0x10,
           'CTRL': 0x11,
           '^': 0x11,
           'ALT': 0x12,
           'A': 0x12,
           'PAUSE': 0x13,
           'CAPSLOCK': 0x14,
           'ESC': 0x1B,
           'SPACEBAR': 0x20,
           ' ': 0x20,
           'PAGE': 0x21,
           'PAGE_DOWN': 0x22,
           'END': 0x23,
           'HOME': 0x24,
           'LEFT': 0x25,
           'UP': 0x26,
           'RIGHT': 0x27,
           'DOWN': 0x28,
           'SELECT': 0x29,
           'PRINT': 0x2A,
           'EXECUTE': 0x2B,
           'PRINT_SCREEN': 0x2C,
           'INS': 0x2D,
           'DEL': 0x2E,
           'HELP': 0x2F,
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
           'NUMPAD_0': 0X60,
           'NUMPAD_1': 0X61,
           'NUMPAD_2': 0X62,
           'NUMPAD_3': 0X63,
           'NUMPAD_4': 0X64,
           'NUMPAD_5': 0X65,
           'NUMPAD_6': 0X66,
           'NUMPAD_7': 0X67,
           'NUMPAD_8': 0X68,
           'NUMPAD_9': 0X69,
           'MULTIPLY_KEY': 0X6A,
           'ADD_KEY': 0X6B,
           'SEPARATOR_KEY': 0X6C,
           'SUBTRACT_KEY': 0X6D,
           'DECIMAL_KEY': 0X6E,
           'DIVIDE_KEY': 0X6F,
           'F1': 0x70,
           'F2': 0x71,
           'F3': 0x72,
           'F4': 0x73,
           'F5': 0x74,
           'F6': 0x75,
           'F7': 0x76,
           'F8': 0x77,
           'F9': 0x78,
           'F10': 0x79,
           'F11': 0x7A,
           'F12': 0x7B,
           'F13': 0x7C,
           'F14': 0x7D,
           'F15': 0x7E,
           'F16': 0x7F,
           'F17': 0x80,
           'F18': 0x81,
           'F19': 0x82,
           'F20': 0x83,
           'F21': 0x84,
           'F22': 0x85,
           'F23': 0x86,
           'F24': 0x87,
           'NUM_LOCK': 0X90,
           'SCROLL_LOCK': 0X91,
           'LEFT_SHIFT': 0XA0,
           'RIGHT_SHIFT ': 0XA1,
           'LEFT_CONTROL': 0XA2,
           'RIGHT_CONTROL': 0XA3,
           'LEFT_MENU': 0XA4,
           'RIGHT_MENU': 0XA5,
           'BROWSER_BACK': 0XA6,
           'BROWSER_FORWARD': 0XA7,
           'BROWSER_REFRESH': 0XA8,
           'BROWSER_STOP': 0XA9,
           'BROWSER_SEARCH': 0XAA,
           'BROWSER_FAVORITES': 0XAB,
           'BROWSER_START_AND_HOME': 0XAC,
           'VOLUME_MUTE': 0XAD,
           'VOLUME_DOWN': 0XAE,
           'VOLUME_UP': 0XAF,
           'NEXT_TRACK': 0XB0,
           'PREVIOUS_TRACK': 0XB1,
           'STOP_MEDIA': 0XB2,
           'TOGGLE_MEDIA': 0XB3,
           'START_MAIL': 0XB4,
           'SELECT_MEDIA': 0XB5,
           'START_APPLICATION_1': 0XB6,
           'START_APPLICATION_2': 0XB7,
           'ATTN_KEY': 0XF6,
           'CRSEL_KEY': 0XF7,
           'EXSEL_KEY': 0XF8,
           'PLAY_KEY': 0XFA,
           'ZOOM_KEY': 0XFB,
           'CLEAR_KEY': 0XFE,
           '+': 0xBB,
           ',': 0xBC,
           '-': 0xBD,
           '.': 0xBE,
           '/': 0xBF,
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