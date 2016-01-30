"""
Drops text formatting
"""

import text_manipulate


def main():
    try:
        text_manipulate.manipulator(lambda text: text, empty_clipboard=True)
    except Exception as e:
        import ipdb;

        ipdb.set_trace()
        input()


if __name__ == "__main__":
    main()