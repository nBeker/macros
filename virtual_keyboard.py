from win32api import keybd_event as keyboard_event
from  win32con import KEYEVENTF_KEYUP as RELEASE_KEY
from time import sleep

SLEEP_CONST = .05

#Giant dictonary to hold key name and VK value
VK_CODE = {'BACKSPACE':0x08,
           'TAB':0x09,
           '\t':0x09,        
           'clear':0x0C,
           'ENTER':0x0D,
           '\n':0x0D,
           'SHIFT':0x10,
           'S':0x10,
           'CTRL':0x11,
           '^':0x11,
           'ALT':0x12,
           'A':0x12,
           'PAUSE':0x13,
           'CAPSLOCK':0x14,
           'ESC':0x1B,
           'SPACE':0x20,
           'PAGE':0x21,
           'PAGE_DOWN':0x22,
           'END':0x23,
           'HOME':0x24,
           'LEFT':0x25,
           'UP':0x26,
           'RIGHT':0x27,
           'DOWN':0x28,
           'SELECT':0x29,
           'PRINT':0x2A,
           'EXECUTE':0x2B,
           'PRINT_SCREEN':0x2C,
           'INS':0x2D,
           'DEL':0x2E,
           'HELP':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           ';':0xBA,
           '[':0xDB,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0}



def press(keys_list):
    '''
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    '''
    for key in keys_list:
        keyboard_event(VK_CODE[key], 0,0,0)
        sleep(SLEEP_CONST)
        keyboard_event(VK_CODE[key],0 ,RELEASE_KEY ,0)

def hold(keys_list):
    '''
    press and hold. Do NOT release.
    accepts as many arguments as you want.
    e.g. pressAndHold('left_arrow', 'a','b').
    '''
    for key in keys_list:
        keyboard_event(VK_CODE[key], 0,0,0)
        sleep(SLEEP_CONST)
           
def release(keys_list):
    '''
    release depressed keys
    accepts as many arguments as you want.
    e.g. release('left_arrow', 'a','b').
    '''
    for key in keys_list:
           keyboard_event(VK_CODE[key],0 ,RELEASE_KEY ,0)


def press_combo(keys_list):
    '''
    press and hold passed in strings. Once held, release
    accepts as many arguments as you want.
    e.g. pressAndHold('left_arrow', 'a','b').

    this is useful for issuing shortcut command or shift commands.
    e.g. pressHoldRelease('ctrl', 'alt', 'del'), pressHoldRelease('shift','a')
    '''
    hold(keys_list)
    release(keys_list)

def typer(string=None,*args):
##    sleep(4)
    for i in string:
        if i == ' ':
            keyboard_event(VK_CODE['spacebar'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['spacebar'],0 ,RELEASE_KEY ,0)

        elif i == '!':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['1'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['1'],0 ,RELEASE_KEY ,0)

        elif i == '@':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['2'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['2'],0 ,RELEASE_KEY ,0)

        elif i == '{':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['['], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['['],0 ,RELEASE_KEY ,0)

        elif i == '?':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['/'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['/'],0 ,RELEASE_KEY ,0)

        elif i == ':':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE[';'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE[';'],0 ,RELEASE_KEY ,0)

        elif i == '"':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['\''], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['\''],0 ,RELEASE_KEY ,0)

        elif i == '}':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE[']'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE[']'],0 ,RELEASE_KEY ,0)

        elif i == '#':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['3'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['3'],0 ,RELEASE_KEY ,0)

        elif i == '$':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['4'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['4'],0 ,RELEASE_KEY ,0)

        elif i == '%':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['5'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['5'],0 ,RELEASE_KEY ,0)

        elif i == '^':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['6'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['6'],0 ,RELEASE_KEY ,0)

        elif i == '&':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['7'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['7'],0 ,RELEASE_KEY ,0)

        elif i == '*':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['8'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['8'],0 ,RELEASE_KEY ,0)

        elif i == '(':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['9'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['9'],0 ,RELEASE_KEY ,0)

        elif i == ')':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['0'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['0'],0 ,RELEASE_KEY ,0)

        elif i == '_':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['-'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['-'],0 ,RELEASE_KEY ,0)


        elif i == '=':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['+'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['+'],0 ,RELEASE_KEY ,0)

        elif i == '~':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['`'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['`'],0 ,RELEASE_KEY ,0)

        elif i == '<':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE[','], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE[','],0 ,RELEASE_KEY ,0)

        elif i == '>':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['.'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['.'],0 ,RELEASE_KEY ,0)

        elif i == 'A':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['a'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['a'],0 ,RELEASE_KEY ,0)

        elif i == 'B':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['b'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['b'],0 ,RELEASE_KEY ,0)

        elif i == 'C':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['c'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['c'],0 ,RELEASE_KEY ,0)

        elif i == 'D':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['d'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['d'],0 ,RELEASE_KEY ,0)

        elif i == 'E':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['e'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['e'],0 ,RELEASE_KEY ,0)

        elif i == 'F':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['f'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['f'],0 ,RELEASE_KEY ,0)

        elif i == 'G':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['g'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['g'],0 ,RELEASE_KEY ,0)

        elif i == 'H':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['h'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['h'],0 ,RELEASE_KEY ,0)

        elif i == 'I':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['i'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['i'],0 ,RELEASE_KEY ,0)

        elif i == 'J':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['j'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['j'],0 ,RELEASE_KEY ,0)

        elif i == 'K':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['k'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['k'],0 ,RELEASE_KEY ,0)

        elif i == 'L':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['l'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['l'],0 ,RELEASE_KEY ,0)

        elif i == 'M':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['m'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['m'],0 ,RELEASE_KEY ,0)

        elif i == 'N':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['n'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['n'],0 ,RELEASE_KEY ,0)

        elif i == 'O':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['o'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['o'],0 ,RELEASE_KEY ,0)

        elif i == 'P':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['p'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['p'],0 ,RELEASE_KEY ,0)

        elif i == 'Q':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['q'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['q'],0 ,RELEASE_KEY ,0)

        elif i == 'R':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['r'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['r'],0 ,RELEASE_KEY ,0)

        elif i == 'S':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['s'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['s'],0 ,RELEASE_KEY ,0)

        elif i == 'T':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['t'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['t'],0 ,RELEASE_KEY ,0)

        elif i == 'U':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['u'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['u'],0 ,RELEASE_KEY ,0)

        elif i == 'V':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['v'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['v'],0 ,RELEASE_KEY ,0)

        elif i == 'W':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['w'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['w'],0 ,RELEASE_KEY ,0)

        elif i == 'X':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['x'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['x'],0 ,RELEASE_KEY ,0)

        elif i == 'Y':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['y'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['y'],0 ,RELEASE_KEY ,0)

        elif i == 'Z':
            keyboard_event(VK_CODE['left_shift'], 0,0,0)
            keyboard_event(VK_CODE['z'], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE['left_shift'],0 ,RELEASE_KEY ,0)
            keyboard_event(VK_CODE['z'],0 ,RELEASE_KEY ,0)

    
        else:    
            keyboard_event(VK_CODE[key], 0,0,0)
            sleep(SLEEP_CONST)
            keyboard_event(VK_CODE[key],0 ,RELEASE_KEY ,0)




