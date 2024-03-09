import os
import subprocess
import importlib.util
import sys
import pyvbox

from OSCreator.Modules.VirtualBoxSDK.sdk.installer import vboxapi

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

import virtualbox as vb
from Modules.VirtualBoxSDK.sdk.installer.vboxapi import *

class VM:
    def __init__(self):
        self.vbox = vboxapi.VirtualBoxManager(None, None)

    def start(self, vname):
        session = self.vbox.openMachineSession(vname, False)

VM()
