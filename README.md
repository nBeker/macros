# macros
Be a better person to your PC

Here are a bunch of scripts that should make your life easier.

There are some cross-dependencies between those scripts so be-aware that not every file here is independent.


Few Installation Tips:
1. Maps your scripts location to the %PYTHONPATH% environment variable

2. Allow Python Files to run without .py extension when calling
(Add .PY to %PATHTEXT% environment variable)

3. Fix python argument passing method 
set:
HKEY_CURRENT_USER\SOFTWARE\Classes\Applications\python.exe\shell\open\command
to:
"C:\Python35\python.exe" "%1" %*
