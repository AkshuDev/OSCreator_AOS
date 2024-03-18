import os
from shutil import ExecError
import subprocess
import importlib.util
import sys
import pyvbox

from vboxapi import VirtualBoxManager

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from LIB import Win

libw = Win

class Dependency:
    @staticmethod
    def checkModules():
        try:
            importlib.util.find_spec('tarfile')
            importlib.util.find_spec('lzma')
            importlib.util.find_spec('pyvmomi')
            importlib.util.find_spec('configparser')
            importlib.util.find_spec('pyvbox')
            importlib.util.find_spec('vboxapi')
            importlib.util.find_spec('virtualbox')
            return True
        except Exception:
            return False

    @staticmethod
    def installModules():
        inp = input('Install Modules [5] (y/n): ').lower()
        if inp == "n":
            raise Exception("Stopping.. All modules required to use OSCreator")
        elif inp == 'y':
            subprocess.run(['pip', 'install', 'tarfile'])
            subprocess.run(['pip', 'install', 'lzma'])
            subprocess.run(['pip', 'install', 'pyvmomi'])
            subprocess.run(['pip', 'install', 'configparser'])
            subprocess.run(['pip', 'install', 'pyvbox'])
            subprocess.run(['pip', 'install', 'vboxapi'])
            subprocess.run(['pip', 'install', 'virtualbox'])
        else:
            exit(1)

    @staticmethod
    def createCONFIG():
        import configparser
        config = configparser.ConfigParser()
        config['Modules'] = {'tarfile': 'installed', 'lzma': 'installed', 'pyvmomi': 'installed', 'configparser':'installed', 'pyvbox': 'installed', 'vboxapi': 'installed', 'virtualbox': 'installed', 'all': 'installed'}
        with open(libw.CONFIG, 'w') as cf:
            config.write(cf)

if os.path.exists(libw.CONFIG) and Dependency().checkModules():
    pass
else:
    if Dependency().checkModules():
        Dependency().createCONFIG()
        exit(0)
    else:
        Dependency().installModules()
        Dependency().createCONFIG()
        exit(0)

class INI():
    def __init__(self) -> None:
        self.file = libw.CONFIG

    @staticmethod
    def reset():
        os.remove(libw.CONFIG)
        raise Exception("Exiting... Please create Restart the script.")

    def settings(self):
        import configparser
        config = configparser.ConfigParser()
        settings = {
            'port': '80',
            'VM_port': '$AOS(vm_specified)',
            'HDisk_port': '81',
        }
        config['settings']

    @staticmethod
    def splitter(cmd: str, flag:str=""):
        if flag == "PC_Code(FILE)":
            cmd = cmd.replace('---@---$AOS(', '')
            cmd = cmd.replace(')---@---', '')
            cmdL = cmd.split('-')
            if not cmdL[0].lower() == "pheonix":
                raise Exception("Invalid Pheonix Code")
            cmd = str(cmdL[1])
            file = ""
            ext = ""
            for char in cmd:
                if char.isupper():
                    file += char
                if char.islower():
                    break
            cmd = cmd.replace(file, '')
            for char_ in cmd:
                if char_.islower():
                    ext += char_
                if char_.isupper():
                    break
            cmd = cmd.replace(ext, '')
            fullfile = file+'.'+ext
            func = ''
            for char__ in cmd:
                if char__.isupper():
                    func += char__
                if char__.isdigit():
                    break
            cmd = cmd.replace(func, '')
            line_no = 0
            for num in cmd:
                if num.isdigit() or num == "0":
                    line_no += int(num)
                if num.isalpha() and num != '0':
                    break

            cmd = cmd.replace(str(line_no), '')
            cmd = cmd.replace('_', '')
            var = ''
            self_ = ''
            callup = ''
            for self__ in cmd:
                if self__.islower():
                    self_ += self__
                if self__.isupper():
                    break
            cmd = cmd.replace(self_, '')
            for var_ in cmd:
                if var_.isupper():
                    var += var_
                if var_.islower():
                    break
            cmd = cmd.replace(var, '')
            for callup_ in cmd:
                if callup_.islower():
                    callup += callup_
                if callup_.isupper():
                    break
            cmd = cmd.replace(callup, '')
            cmdL = {
                'file': fullfile,
                'function': func,
                'line_no': line_no,
                'self': self_,
                'variable': var,
                'call': callup
            }
            return cmdL

    def dict_(self, cmd: list, flag:str=""):
        from LIB import Dictionary as Dict
        from LIB import logger as log
        if flag == 'find':
            for i, cmd_ in cmd:
                if '---@---$AOS(' in cmd_ and ')---@---' in cmd_:
                    tokens = self.splitter(cmd_, 'PC_Code(FILE)')
                    return tokens
                else:
                    if Dict().cmds() in cmd_:
                        if Dict().checkFORMAT(cmd_):return True
                        else:return False
        else:
            raise Exception(f'{log("", "Wrong Command given", "dict_", "INI", "VM.py", "OSCreator")}')

    def parse(self, cmd: list, flag:str=""):
        tokens = self.dict_(list('find'),flag)
        if tokens:
            pass
        else:
            raise Exception('Sorry direct [parse] calls are system hazard!')

    def run(self, cmd: str):
        cmd = cmd.strip(" ")
        if self.dict_(list(cmd)):
            self.parse(list(cmd), "---@---$AOS(pheonix-VMpyINIT6_selfCMD:parse)---@---")

import virtualbox as vb
from virtualbox.library import *
import vboxapi as vboxapi

class VM:
    def __init__(self):
        self.vboxMGR = VirtualBoxManager(None,  None)
        self.vbox = vb.VirtualBox()

    def start(self, vm_name, path=""):
        vmS = vb.Session()
        vmM = self.vbox.create_machine(vm_name, "MyVM OS", [], 'Other', '')
        #configue
        vmM.memory_size = 100
        vmM.cpu_count = 1
        #V Hard disk
        #vdi_format =
        vdi_location = path
        vdi_access_mode = "ReadWrite"
        vdi_device_type = DeviceType("HardDisk")
        #vdi = self.vbox.create_medium(MediumVariant("VDI"), vdi_path, [])
        #vmM.attach_device("SATA", INI().run('pheonix -cmd get --p --hdisk'), vdi_device_type, )


        progress = vmM.launch_vm_process(vmS, "gui", [])
        progress.wait_for_completion(10)
