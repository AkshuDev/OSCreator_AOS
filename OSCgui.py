import OpenGL
import os
import subprocess
import sys
import PyQt5 as pyqt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from ctypes import *

import platform
import psutil

import qemu
from qemu import *
from qemu.qmp import QMPClient
#

class OSCMainVM():
    def __init__(self):
        super().__init__()

        self.InitVM()

    def InitVM(self):
        self.GSI()


    def GSI(self):
        os = platform.system()

        if os == "Windows":
            self.GSI_HW_WIN()
            self.GSI_SW_WIN()
        elif os == "Linux":
            print("Sorry but this OS is currently not optimized for this [software]")
            exit(1)
        else:
            print("Sorry unsupported OS")
            exit(1)

    def GSI_HW_WIN(self):
        # INIT
        self.system_info = {}

        # Get CPU
        self.system_info['cpu'] = os.cpu_count()

        # Get ram
        try:
            result = subprocess.run(['wmic', 'OS', 'get', 'TotalVisibleMemorySize'], capture_output=True, text=True, check=True)
            total_memory_str = result.stdout.splitlines()
            total_memory_str = [total_memory_str.strip() for total_memory_str in total_memory_str if total_memory_str.strip().isdigit()]
            total_memory_str = total_memory_str[0]
            if total_memory_str:
                total_memory = int(total_memory_str)
                total_memory = total_memory / (1024 ** 3) * 1000
                print(f'RAM: [{total_memory}]')
                self.system_info['ram'] = total_memory
            else:
                raise Exception("!!!Stop!!!")
        except (subprocess.CalledProcessError, ValueError) as e:
            raise Exception("Sorry Error in Starting VM code - [OSCreator.GUI.OSCGui/ramVM-t001]")

        # Get hard disk space
        try:
            tdsb = subprocess.run(['wmic', 'diskdrive', 'get', 'size'], capture_output=True, text=True, check=True)
            tdsb = tdsb.stdout.splitlines()
            tds = [tds.strip() for tds in tdsb if tds.strip().isdigit()]
            tds = int(tds[0])
            if tds:
                tds = tds / (1024 ** 3)
                print(f"DISK [{tds}]")
                self.system_info['disk'] = tds
            else:
                raise Exception("!!!Stop!!!")
        except Exception:
            raise Exception("Sorry Error in Starting VM code - [OSCreator.GUI.OSCGui/diskVM-t001]")

        print(self.system_info)

    def GSI_SW_WIN(self):
        self.system_info['os'] = platform.platform()

        net_info = psutil.net_if_addrs()
        self.system_info['network'] = {name: [addr.address for addr in addrs if addr.family == psutil.AF_LINK]
                                       for name, addrs in net_info.items()}

        print(self.system_info)

vm = OSCMainVM()
