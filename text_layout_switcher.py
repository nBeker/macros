from sys import argv as arguments

import text_manipulate
import layout_switcher


def main(flip_clipboard=False, mark_all=False):
    try:
        if flip_clipboard:
            text_manipulate.manipulator(function=layout_switcher.switch_layout)
        else:
            text_manipulate.manipulator_with_keyboard(function=layout_switcher.switch_layout, replace_source=True,
                                                      mark_all=mark_all)
    except Exception as e:
        import ipdb;

        ipdb.set_trace()
        input()


if __name__ == "__main__":
    flip_clipboard = False
    mark_all = False
    if len(arguments) > 1:
        if arguments[1] in "clip":
            flip_clipboard = True
        elif arguments[1] in "all":
            mark_all = True

    main(flip_clipboard=flip_clipboard, mark_all=mark_all)