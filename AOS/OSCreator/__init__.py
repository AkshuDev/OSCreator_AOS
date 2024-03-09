import os
import Library
import LIB

class Error:
    def __init__(ErrorLABEL: str, ErrorMSG: str):
        super().__init__(ErrorLABEL+": "+ErrorMSG)

class Kernal:
    def __init__(self, path: str, arch="0x80", filename="untitled"):
        self.avail_archs = ["0x80"]

        if not arch in self.avail_archs:
            raise Error("Architechture Error", f"Architechure [{arch}] is not in architechure list [{self.avail_archs}]")

        self.path = path
        self.arch = arch
        self.filename = filename

    def make_kernal(self):
        full_path = os.path.join(self.path, self.filename+".asm")
        with open(full_path, "w") as kernel:
            content = Library.kernel_x80
            kernel.write(content)

    def make_bootloader(self):
        full_path = os.path.join(self.path, self.filename+".asm")
        with open(full_path, "w") as bootloader:
            bootloader.write(Library.bootloader_x80)

    def make_IDT(self):
        full_path = os.path.join(self.path, self.filename+".asm")
        with open(full_path, "w") as IDT:
            IDT.write(Library.IDT_x80)