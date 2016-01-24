HEBREW_LAYOUT = {"'": 'w',
                 ',': "'",
                 '.': '/',
                 '/': 'q',
                 '[': ']',
                 '\\': '\\',
                 ']': '[',
                 'א': 't',
                 'ב': 'c',
                 'ג': 'd',
                 'ד': 's',
                 'ה': 'v',
                 'ו': 'u',
                 'ז': 'z',
                 'ח': 'j',
                 'ט': 'y',
                 'י': 'h',
                 'ך': 'l',
                 'כ': 'f',
                 'ל': 'k',
                 'ם': 'o',
                 'מ': 'n',
                 'ן': 'i',
                 'נ': 'b',
                 'ס': 'x',
                 'ע': 'g',
                 'ף': ';',
                 'פ': 'p',
                 'ץ': '.',
                 'צ': 'm',
                 'ק': 'e',
                 'ר': 'r',
                 'ש': 'a',
                 'ת': ','}

ENGLISH_LAYOUT = {HEBREW_LAYOUT[key]: key for key in HEBREW_LAYOUT}


def switch_layout(string):
    source_layout = ENGLISH_LAYOUT if string[0] in ENGLISH_LAYOUT else HEBREW_LAYOUT
    return "".join([source_layout.get(char, char) for char in string])