import virtual_keyboard
import win32clipboard as clipboard

def manipulator(function):
	try:
		# Alt + Tab to return to the previous context
		virtual_keyboard.press_combo("A\t")
		# Ctrl+A+X to Cut all text
		virtual_keyboard.press_combo("^ax")	
	
		clipboard.OpenClipboard()
		data = clipboard.GetClipboardData()
		clipboard.SetClipboardText(function(data), clipboard.CF_UNICODETEXT)

	except Exception as e:
		# Alt + Tab to return to the python context
		virtual_keyboard.press_combo("A\t")
		import ipdb
		print(e.args)
		ipdb.set_trace()
		input()
	finally:
		clipboard.CloseClipboard()
		# Ctrl+V to Paste the new text
		virtual_keyboard.press_combo("^v")