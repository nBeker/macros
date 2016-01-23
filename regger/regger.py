import winreg
import sys

PYTHON_RUNNER         = r'cmd /c python "{script_path}" "{argument_format}"'
REGISTRY_BASE_PATH 	  = r'{extension}\shell\{key_name}'
REGISTRY_CMD		  = r'\command'
ALL_FILE_EXTENSIONS   = '*'
REG_DIRECTORY 		  = 'Directory'
DIRECTORY_BACKGROUND  = 'Directory\Background'
DEFAULT_ARGUMENT      = '%1'
DIRECTORY_BG_ARGUMENT = '%V'

def yes_no_prompt(prompt, default_yes=True):
	if default_yes:
		answer = input(prompt + "[Y / n]")
		return answer.lower() not in ('n', 'no')
	else:
		answer = input(prompt + "[y / N]")
		return answer.lower() not in ('y', 'yes')

def register(script_path, registry_name, context_menu_name=None, extensions=[ALL_FILE_EXTENSIONS, REG_DIRECTORY, DIRECTORY_BACKGROUND]):
	print("Script: %s" % script_path)
	print("Registery Key: %s" % registry_name)
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
		handle.Close()
		handle = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, registry_key_path + REGISTRY_CMD)
		argument = DEFAULT_ARGUMENT if extension is not DIRECTORY_BACKGROUND else DIRECTORY_BG_ARGUMENT
		winreg.SetValueEx(handle, None, 0, winreg.REG_SZ, PYTHON_RUNNER.format(script_path=script_path, argument_format=argument))
		handle.Close()

if __name__ == "__main__":
	extensions = [ALL_FILE_EXTENSIONS, REG_DIRECTORY, DIRECTORY_BACKGROUND]
	
	if len(sys.argv) < 3:
		print("regger.py <script_path> <registry_name> [context_menu_name] [extensions]")
		sys.exit()
	elif len(sys.argv) is 5:
		extensions = sys.argv[4].split(',')
	
	register(sys.argv[1], sys.argv[2], sys.argv[3], extensions)