from layout_switcher import switch_layout
import shutil
import sys
import os

SHORTCUT_PATH = r"C:\shortcuts"
SCRIPT_DIRECTORY = os.path.dirname(__file__)
vbs_path = os.path.join(SCRIPT_DIRECTORY, "linker.vbs")
REGGER_PATH = os.path.join(os.path.dirname(SCRIPT_DIRECTORY), "regger")
INVOKE_VBS_CMD = "cscript %s {0} {1}" % vbs_path

def yes_no_prompt(prompt, default_yes=True):
	if default_yes:
		answer = input(prompt + "[Y / n]")
		return answer.lower() not in ('n', 'no')
	else:
		answer = input(prompt + "[y / N]")
		return answer.lower() not in ('y', 'yes')

def main(path):
	print("File: %s" % path)
	while True:
		link_name = input("Enter link: ")
		if not link_name:
			break

		link_path = SHORTCUT_PATH % link_name
		hebrish_link_path = SHORTCUT_PATH % switch_layout(link_name)
		if not os.path.isfile(link_path) or \
		yes_no_prompt("Link already exist, replace it?"):
			os.system(INVOKE_VBS_CMD.format(path, link_path))
			print("Shortcut created!")

		if not os.path.isfile(hebrish_link_path) or \
		yes_no_prompt("Hebrish link already exist, replace it?"):
			shutil.copy(link_path, hebrish_link_path)
			print("Hebrish shortcut created!")


def register():
	sys.path.append(REGGER_PATH)
	import regger
	print("Successfully imported regger")
	regger.register(__file__, "linker", "Linker")
	print("Successfully registered linker to context menu")


if __name__ == "__main__":
	if len(sys.argv) < 2:
		register()
	else:
		main(sys.argv[1])
		input("(:")