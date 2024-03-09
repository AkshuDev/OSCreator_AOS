import os

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