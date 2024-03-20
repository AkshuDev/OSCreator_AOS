import os
import LIB

class PCT_D_():
    def __init__(self):
        self.cwd = ''
        self.inp = ''

    def init(self):
        self.cwd = os.getcwd()

    def shell_(self):
        self.inp = input(f"PCT$ | {self.cwd}\n")

    def parse_(self):
        from VM.VM import INI
        if not self.inp == "$stop":
            ini = INI()
            ini.run(self.inp)
        else:
            print("BYE!")
            exit(0)

    def run(self):
        while True:
            self.shell_()
            self.parse_()
