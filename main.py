#!/usr/bin/env python3

from verify import *
from menus import supportedProtocol, protocol, mainMenu



realpath = (os.path.dirname(os.path.realpath(__file__)))
BIN = realpath + "/bin"
PROT = realpath + "/protocols"


def main():
    os.system('clear')
    while True:
        mainMenu()
        try:
            answer = int(input("Choose option: "))
        except ValueError:
            print("No valid integer! Please try again ...")
            exit(1)
        if answer == 1:
            print("List of benchmarks")
            supportedProtocol()
        elif answer == 2:
            protocolToVerify = protocol()
            attackVersion(protocolToVerify)
        elif answer == 3:
            print("Exit")
            exit(0)
        else:
            print("Bad option")
            exit(-1)


main()
