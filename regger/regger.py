import os
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
        parser.add_argument("extensions", type=str, nargs='*', default=DEFAULT_EXTENSIONS,
                            help="Which extensions to register the script upon. "
                                 "default:{exts}".format(exts=DEFAULT_EXTENSIONS))
        users = parser.add_mutually_exclusive_group()
        users.add_argument("-o", "--only_me", dest="all_users", action="store_false")
        users.add_argument("-a", "--all_users", dest="all_users", default=True, action="store_true")

    parser = argparse.ArgumentParser(prog="regger",
                                     description="Fast Registry Operations")
    parser.add_argument("registry_name", type=str, help="The key name in the registry")
    subparsers = parser.add_subparsers(dest="action", help='sub-command help')
    subparsers.required = True
    register = subparsers.add_parser('register', help='registers a script to the context menu')
    register.add_argument("script_path", type=str, help="Path of the script you would like to register")

    add_common_args(register)

    register.add_argument("-n", "--friendly_name", type=str, help="The name that will appear to the user",
                          required=False)
    register.add_argument("-i", "--icon", type=str, help="Path to .ICO image", required=False)

    unregister = subparsers.add_parser('unregister', help='registers a script to the context menu')
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
             extensions=(ALL_FILE_EXTENSIONS, REG_DIRECTORY, DIRECTORY_BACKGROUND), icon_path=None,
             root_key=winreg.HKEY_LOCAL_MACHINE):
    """
    Registers a script to right-click context-menu of the relevant extensions
    :param script_path: The script path
    :param registry_name: The registry key name - how it will actually appear in the registry
    :param context_menu_name: How will it look like in the right-click context menu
    :param extensions: Iterable structure of extensions to whom the script will be registered to.
    :param icon_path: path to ICO image file
    :param root_key: HKEY_LM / HKEY_CU
    """
    assert root_key in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER), "Root key must be current_user " \
                                                                              "or local_machine"

    # assert os.path.isfile(script_path), "Given script doesn't exist on system, this might cause problems"
    assert not icon_path or os.path.isfile(icon_path), "Given ico doesn't exist on system, this might cause problems"

    print("Script: %s" % script_path)
    print("Registry Key: %s" % registry_name)
    print("Extensions: [%s]" % ','.join(extensions))
    print("All_users: [%s]" % (root_key is winreg.HKEY_LOCAL_MACHINE))

    if not yes_no_prompt("Sure you want to register the script to all these extensions?"):
        print("Aborting!")
        sys.exit()

    if not context_menu_name:
        context_menu_name = registry_name

    for extension in extensions:
        registry_key_path = REGISTRY_BASE_PATH.format(extension=extension, key_name=registry_name)
        print("Registry path: [%s]" % registry_key_path)
        handle = winreg.CreateKeyEx(root_key, registry_key_path, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(handle, None, 0, winreg.REG_SZ, context_menu_name)
        if icon_path:
            winreg.SetValueEx(handle, ICON, 0, winreg.REG_SZ, icon_path)

        handle.Close()

        handle = winreg.CreateKeyEx(root_key, registry_key_path + REGISTRY_CMD)
        argument = DEFAULT_ARGUMENT if extension is not DIRECTORY_BACKGROUND else DIRECTORY_BG_ARGUMENT
        winreg.SetValueEx(handle, None, 0, winreg.REG_SZ,
                          PYTHON_RUNNER.format(script_path=script_path, argument_format=argument))
        handle.Close()


def unregister(registry_name, extensions=(ALL_FILE_EXTENSIONS, REG_DIRECTORY, DIRECTORY_BACKGROUND),
               root_key=winreg.HKEY_LOCAL_MACHINE):
    """

    :param registry_name:
    :param extensions:
    :param root_key:
    """
    assert root_key in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER), "Root key must be current_user " \
                                                                              "or local_machine"

    print("Registry Key: %s" % registry_name)
    print("Extensions: [%s]" % ','.join(extensions))
    print("All_users: [%s]" % (root_key is winreg.HKEY_LOCAL_MACHINE))

    if not yes_no_prompt("Sure you want to unregister the script to all these extensions?"):
        print("Aborting!")
        sys.exit()

    for extension in extensions:
        registry_key_path = REGISTRY_BASE_PATH.format(extension=extension, key_name=registry_name)
        print("Registry path: [%s]" % registry_key_path)
        handle = winreg.OpenKeyEx(root_key, None, 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteKey(handle, registry_key_path + REGISTRY_CMD)
        winreg.DeleteKey(handle, registry_key_path)
        handle.Close()


if __name__ == "__main__":
    args = handle_arguments()
    root_key = winreg.HKEY_LOCAL_MACHINE if args.all_users else winreg.HKEY_CURRENT_USER

    if args.action == "register":
        register(script_path=args.script_path, registry_name=args.registry_name, context_menu_name=args.friendly_name,
                 extensions=args.extensions, icon_path=args.icon, root_key=root_key)

    elif args.action == "unregister":
        unregister(registry_name=args.registry_name, extensions=args.extensions, root_key=root_key)
