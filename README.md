# macros
Be a better person to your PC

Here are a bunch of scripts that should make your life easier.

There are some cross-dependencies between those scripts so be-aware that not every file here is independent.

What's In:

Linker - a fast shortcut creator for windows, designed to enable a user to create as many shortcuts to every program, site or directory.
         the point of this script is to create the shortcuts on a %PATH% mapped directory which will allow them to be invoked from Run             context (Win + R)
         
Regger - Helps register scripts \ apps to right-click context-menu

simple_clipboard - a simplified text-wrapper api for win32clipboard, supports only get, set, empty

virtual_keyboard - wrapper for win32api virtual keyboard

text_manipulte - performs a function on a clipboard text. features a keyboard mode which also cuts and pastes after manipulation

layout_swithcer - Hebrew <-> English keyboard layout switcher

Few Installation Tips:

1. Maps your scripts location to the %PYTHONPATH% environment variable

2. Allow Python Files to run without .py extension when calling
(Add .PY to %PATHTEXT% environment variable)

3. Fix python argument passing method 
set:
HKEY_CURRENT_USER\SOFTWARE\Classes\Applications\python.exe\shell\open\command
to:
"C:\Python35\python.exe" "%1" %*


Apps:

1. Everything
2. Totalcommander
3. SublimeText
4. MPC-HC
5. Conemu
