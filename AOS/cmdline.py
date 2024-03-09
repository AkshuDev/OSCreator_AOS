import os

class AOS_CMDL:
    def __init__(self, cmd):
        self.cmd = cmd
        self.cmdList = ['assoc', 'attrib', 'aol', 'hacline', 'bcdboot']
        self.parser()

    def parser(self):
        if not self.cmd in self.cmdList:
            raise Exception(f"No such command found [{self.cmd}] in [{self.cmdList}]!")
        cmd = self.cmd

        if cmd == "assoc":
            #do something
            pass
        elif cmd == "attrib":
            #do something
            pass
        elif cmd == "aol":
            #strat AOL
            pass
        elif cmd == "hacline":
            #start HaCline
            pass
        elif cmd == "bcdboot":
            #do something
            pass