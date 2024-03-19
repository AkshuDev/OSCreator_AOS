from datetime import date
import os
from xmlrpc.client import Boolean

OSCreatorID = u"pheonixstudios.oscreator.gui.0.1"

class Win:
    OSC_P = "OSCreator"
    VM_P = os.path.join(OSC_P, "VM")
    Time_P = os.path.join(OSC_P, "Time")
    old_projects_P = os.path.join(OSC_P, "old_projects")
    GUI_P = os.path.join(OSC_P, "GUI")
    Assets_P = os.path.join(OSC_P, "Assets")
    #Files
    OSCGui = os.path.join(GUI_P, "OSCgui.py")
    PSICO = os.path.join(Assets_P, "PheonixStudios.ico")
    PSPNG = os.path.join(Assets_P, "PheonixStudios.png")
    Projects = os.path.join(old_projects_P, "Projects.txt")
    VM = os.path.join(VM_P, "VM.py")
    INIT = os.path.join(OSC_P, "__init__.py")
    Gui = os.path.join(OSC_P, "Gui.py")
    Library = os.path.join(OSC_P, "Library.py")
    CONFIG = os.path.join(OSC_P, "settings.ini")

class Dictionary:
    def __init__(self) -> None:
        self.cmds_ = ['check INI', 'write INI', 'delete INI', 'check INI --full', 'write INI --full', 'delete INI --all --instances']
        self.cmdL_ = ['file', 'function', 'line_no', 'self', 'variable', 'call']
        self.iniSEC_ = ['Modules']
        self.moduleDATA = ['tarfile', 'lzma', 'pyvmomi', 'configparser', 'pyvbox', 'vboxapi', 'virtualbox', 'datetime', 'all']
        self.formats = {
            'check INI': 'check INI "path" ;value;',
            'write INI': 'write INI "path" ;value;',
            'delete INI': 'delete INI "path"',
            'check INI --full': 'check INI --full "path"',
            'write INI --full': 'write INI --full "path"',
            'delete INI --all --instances': 'delete INI --all --instances "path"',
        }

    def cmds(self) -> list:
        return self.cmds_

    def cmdL(self) -> list:
        return self.cmdL_

    def iniSEC(self) -> list:
        return self.iniSEC_

    def getDATA_SEC(self, section:str) -> list:
        if section == "Modules":
            return self.moduleDATA
        return []

    def checkFORMAT(self, cmd:str) -> bool:
        for i, v in enumerate(self.cmds_):
            idx = 0
            format_ = self.formats[v]
            for char in format_:
                if char in cmd and not idx > 0:
                    continue
                elif idx == 1:
                    continue
                elif char == '"' and idx == 0:
                    idx = 1
                elif char == '"' and idx == 1:
                    idx = 0
                elif char == ';' and idx == 0:
                    idx = 1
                elif char == ';' and idx == 1:
                    idx = 0
                else:
                    return False
        return True

class logger():
    def __init__(self, flag, msg, *args) -> None:
        from datetime import datetime
        from datetime import date
        fullcmd = f'T:[{datetime.now().strftime("%H:%M:%S")}] D:[{date.today()}] MSG:[{msg}] CALL['
        for i, v in enumerate(args):
            if flag == '' or flag == 'EXCEPTION':
                if i != 0:
                    fullcmd += '-' + v
                else:
                    fullcmd += v
            else:
                if i != 0:
                    fullcmd += ' ' + v
                else:
                    fullcmd += v
        fullcmd += ']'
        print(fullcmd)
