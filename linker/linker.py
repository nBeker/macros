import shutil
import sys
import os
# Layout swticher is an Hebrew-English keyboard translator.
# This make sure every link created in both keyboard layouts
from layout_switcher import switch_layout

# Location of shortcuts folder.
# Don't forget to add it to the %PATH% environment variable.
SHORTCUT_PATH = r"C:\shortcuts\%s.lnk"
# Determining the path where this script resides
INVOKE_VBS_CMD = 'cscript %s "{0}" "{1}"' % os.path.join(os.path.dirname(__file__), "linker.vbs")


def yes_no_prompt(prompt, yes_default=True):
    """
    Prompts a Yes \ No question to the user
    :param prompt: The question to the user
    :param yes_default: Whether yes will be the default answer
    :return: True \ False if answer satisfies the `default` argument.
    """
    if yes_default:
        answer = input(prompt + "[Y / n]")
        return answer.lower() not in ('n', 'no')
    else:
        answer = input(prompt + "[y / N]")
        return answer.lower() not in ('y', 'yes')


def main(path):
    """
    Creates shortcuts for a specific File or Folder for faster access
    :param path: the object to creates shortcuts to.
    """
    print("File: %s" % path)
    while True:
        link_name = input("Enter link: ")
        if not link_name:
            break

        link_path = SHORTCUT_PATH % link_name
        hebrish_link_path = SHORTCUT_PATH % switch_layout(link_name)

        if not os.path.isfile(link_path) or yes_no_prompt("Link already exist, replace it?"):
            os.system(INVOKE_VBS_CMD.format(path, link_path))
            print("Shortcut created!")

        # Super Lazy Hack:
        # Copy the shortcut created to a name with the same keystrokes on hebrew layout
        if not os.path.isfile(hebrish_link_path) or yes_no_prompt("Hebrish link already exist, replace it?"):
            shutil.copy(link_path, hebrish_link_path)
            print("Hebrish shortcut created!")


def register():
    """
    Registers the linker script from it's current location to the right click context menu.
    The script will be registered for the [*, Directory, Directory\Background] context menus sby default.
    """
    import regger

    print("Successfully imported regger")
    regger.register(__file__, "linker", "Linker")
    print("Successfully registered linker to context menu")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # If no parameters given, register linker to the context menu
        register()
    elif os.path.exists(sys.argv[1]) or "http" in sys.argv[1]:
        # If given path exists, create links..
        main(sys.argv[1])
        input("(:")