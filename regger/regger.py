import sys
import winreg
import argparse

PYTHON_RUNNER = r'cmd /c python "{script_path}" "{argument_format}"'
REGISTRY_BASE_PATH = r'SOFTWARE\Classes\{extension}\shell\{key_name}'
REGISTRY_CMD = r'\command'
ALL_FILE_EXTENSIONS = '*'
REG_DIRECTORY = 'Directory'
DIRECTORY_BACKGROUND = 'Directory\\Background'
DEFAULT_EXTENSIONS = (ALL_FILE_EXTENSIONS, REG_DIRECTORY, DIRECTORY_BACKGROUND)
DEFAULT_ARGUMENT = '%1'
DIRECTORY_BG_ARGUMENT = '%V'
ICON = "Icon"

def handle_arguments():
    def add_common_args(parser):
        parser.add_argument("registry_name", type=str, help="The key name in the registry")
        parser.add_argument("extensions", type=str, nargs='*', default=DEFAULT_EXTENSIONS,
                             help="Which extensions to register the script upon. "
                               "default:{exts}".format(exts=DEFAULT_EXTENSIONS))
        users = parser.add_mutually_exclusive_group()
        users.add_argument("-o", "--only_me", dest="all_users",action="store_false")
        users.add_argument("-a", "--all_users", dest="all_users", default=True, action="store_true")

    parser = argparse.ArgumentParser(prog="regger",
                                     description="Fast Registry Operations")
    subparsers = parser.add_subparsers(help='sub-command help')

    register = subparsers.add_parser('register', help='registers a script to the context menu')
    register.set_defaults(action="register")
    register.add_argument("script_path", type=str, help="Path of the script you would like to register")

    add_common_args(register)

    register.add_argument("-n", "--friendly_name", type=str, help="The name that will appear to the user",
                          required=False)
    register.add_argument("-i", "--icon", type=str, help="Path to .ICO image", required=False)


    unregister = subparsers.add_parser('unregister', help='registers a script to the context menu')
    unregister.set_defaults(action="unregister")
    add_common_args(unregister)

    return parser.parse_args()

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


def register(script_path, registry_name, context_menu_name=None,
             extensions=(ALL_FILE_EXTENSIONS, REG_DIRECTORY, DIRECTORY_BACKGROUND), icon_path=None):
    """
    Registers a script to right-click context-menu of the relevant extensions
    :param script_path: The script path
    :param registry_name: The registry key name - how it will actually appear in the registry
    :param context_menu_name: How will it look like in the right-click context menu
    :param extensions: Iterable structure of extensions to whom the script will be registered to.
    :param icon_path: path to ICO image file
    """
    print("Script: %s" % script_path)
    print("Registry Key: %s" % registry_name)
    print("Extensions: [%s]" % ','.join(extensions))

    if not yes_no_prompt("Sure you want to register the script to all these extensions?"):
        print("Aborting!")
        sys.exit()

    if not context_menu_name:
        context_menu_name = registry_name

    for extension in extensions:
        registry_key_path = REGISTRY_BASE_PATH.format(extension=extension, key_name=registry_name)
        handle = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, registry_key_path, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(handle, None, 0, winreg.REG_SZ, context_menu_name)
        if icon_path:
            winreg.SetValueEx(handle, ICON, 0, winreg.REG_SZ, icon_path)

        handle.Close()

        handle = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, registry_key_path + REGISTRY_CMD)
        argument = DEFAULT_ARGUMENT if extension is not DIRECTORY_BACKGROUND else DIRECTORY_BG_ARGUMENT
        winreg.SetValueEx(handle, None, 0, winreg.REG_SZ,
                          PYTHON_RUNNER.format(script_path=script_path, argument_format=argument))
        handle.Close()


if __name__ == "__main__":
    args = handle_arguments()
    root_key = winreg.HKEY_LOCAL_MACHINE if args.all_users else winreg.HKEY_CURRENT_USER
    if args.action == "register":
        register(script_path=args.script_path, registry_name=args.registry_name, context_menu_name=args.friendly_name,
                 extensions=args.extensions, icon_path=args.icon)

    elif args.action == "unregister":
        pass
