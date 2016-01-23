' Optional Parameters commented out
' 1st Argument: Orginal file path
' 2nd Argument: Destination link path


Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = WScript.Arguments(1)
Set oLink = oWS.CreateShortcut(sLinkFile)

oLink.TargetPath = WScript.Arguments(0)
'	oLink.Arguments = ""
'	oLink.Description = "MyProgram"
'	oLink.HotKey = "ALT+CTRL+F"
'	oLink.IconLocation = "C:\Program Files\MyApp\MyProgram.EXE, 2"
'	oLink.WindowStyle = "1"
'	oLink.WorkingDirectory = "C:\Program Files\MyApp"
oLink.Save