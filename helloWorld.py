from winreg import *


def read_from_registry():
    try:
        root_key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\WOW6432Node\ProtectMyTech', 0, KEY_READ)
        test = (QueryValueEx(root_key, "FilePath"))
        print(test[0])
        CloseKey(root_key)
        if "" == test:
            raise WindowsError
    except WindowsError:
        print("Oops")



# import pywinauto
# import time
# from pywinauto.application import Application
# app = Application(backend="uia").start(cmd_line= "C:\ProgramData\Accenture\ProtectMyTech\ProtectMyTech.exe")
# time.sleep(10)
# # app.window(Name="Protect myTech").child_window(AutomationId='btnGoogleChromeCheck').click_input()
#
# main_dlg = app.window(Name="Protect myTech")
# main_dlg.print_control_identifiers()



import pywinauto
import time
from pywinauto.application import Application
app = Application(backend="uia")
app.start(cmd_line= "C:\ProgramData\Accenture\ProtectMyTech\ProtectMyTech.exe")
time.sleep(10)
# app.window(Name="Protect myTech").child_window(AutomationId='btnGoogleChromeCheck').click_input()

main_dlg = app.window(Name="Protect myTech")
# dlg = app.windows()
# print(dlg)

dlg = app['Protect myTech']
dlg.print_control_identifiers()