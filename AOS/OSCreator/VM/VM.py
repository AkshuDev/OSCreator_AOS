import os
from shutil import ExecError
import subprocess
import importlib.util
import sys
import pyvbox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vboxapi import VirtualBoxManager
from LIB import Win
import LIB

libw = Win

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

    def dict_(self, cmd:list, flag=""):
        from LIB import Dictionary as Dict
        from LIB import logger as log
        if flag == 'find':
            for i, cmd_ in enumerate(cmd):
                if '---@---$AOS(' in cmd_ and ')---@---' in cmd_:
                    tokens = self.splitter(cmd_, 'PC_Code(FILE)')
                    return tokens
                else:
                    if cmd_ in Dict().cmds():
                        if Dict().checkFORMAT(cmd_):return {'correct': 'true'}
                        else:return None
        else:
            raise Exception(log("", "Wrong Command given", "dict_", "INI", "VM.py", "OSCreator"))

    def parse(self, cmd_: list, flag:str=""):
        for i,cmd in enumerate(cmd_):
            tokens = self.dict_(list('find'),flag)
            if tokens:
                for i,v in enumerate(LIB.Dictionary().cmdL()):
                    if tokens[v]:
                        pass
                    else:
                        raise Exception(LIB.logger('', 'Wrong [PC_CODE] ', 'parse', 'INI', 'VM.py', 'OSCreator'))
                if cmd:
                    if self.dict_(list(cmd), "find"):
                        if 'check INI' in cmd:
                            cmd = cmd.replace('check INI ')
                            if "--full" in cmd:
                                output = dict()
                                cmd = cmd.replace("--full ", '')
                                cmd = cmd.replace('"', '')
                                path = cmd
                                from configparser import ConfigParser
                                try:
                                    config = ConfigParser()
                                    file = open(path, "r")
                                    config.read_file(path)
                                    sections = config.sections()
                                    for section in sections:
                                        items = config.items(section)
                                        output[section] = dict(items)
                                    for i,v in enumerate(LIB.Dictionary().iniSEC()):
                                        if output[v]:
                                            for i_,v_ in enumerate(LIB.Dictionary().getDATA_SEC(v)):
                                                if output[v][v_]:
                                                    if v == "Modules":
                                                        if i == len(LIB.Dictionary().getDATA_SEC(v)):
                                                            if output[v][v_] == "installed":
                                                                return True
                                                            else:
                                                                return False
                                                        else:
                                                            pass
                                                else:
                                                    return False
                                        else:
                                            return False
                                    return True
                                except Exception:
                                    raise Exception(LIB.logger('', 'Wrong [PATH] ', 'parse', 'INI', 'VM.py', 'OSCreator'))
                    else:
                        raise Exception(LIB.logger('', 'Wrong [CMD] ', 'parse', 'INI', 'VM.py', 'OSCreator'))
                else:
                    raise Exception(LIB.logger('', '[CMD] Not Given', 'parse', 'INI', 'VM.py', 'OSCreator'))
            else:
                raise Exception('Sorry direct [parse] calls are system hazard!')

    def run(self, cmd: str, cmdL: list=[]):
        if cmd:
            cmd = cmd.strip(" ")
            if self.dict_(list(cmd), "find"):
                self.parse(list(cmd), "---@---$AOS(pheonix-VMpyINIT4_selfCMD:parse)---@---")
        else:
            if cmdL:
                for i, cmd in enumerate(cmdL):
                    cmd = cmd.strip(" ")
                    if self.dict_(list(cmd), "find"):
                        self.parse(list(cmd), "---@---$AOS(pheonix-VMpyINIT4_selfCMD:parse)---@---")
            else:
                raise Exception(LIB.logger('', 'No Command("CMD")', 'INI', 'VM.py', 'OSCreator'))

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
