def mainMenu():
    print("*************************************************************************************************")
    print("MENU:")
    print("1) List of supported benchmarks")
    print("2) Verify")
    print("3) Exit")
    print("*************************************************************************************************")

def protocol():
    supportedProtocol()
    try:
        result = int(input("Choose protocol: "))
        if result < 1 or result > 19:
            print("You choose bad option")
            exit(1)
        return result
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)

def supportedProtocol():
    print("1) Timed version of Needham Schroeder Public Key Protocol")
    print("2) Timed version of Wide Mouthed Frog Protocol")
    print("3) Timed version of Denning-Sacco Protocol")
    print("4) Timed version of Kao-Chow Protocol")
    print("5) Timed version of Carlsen's Secret Key Initiator Protocol")
    print("6) Timed version of Needham Schroeder Symetric Key Protocol")
    print("7) Timed version of Yahalom Protocol")
    print("8) Timed version of the Lowe's modification of Needham Schroeder Public Key Protocol")
    print("9) Timed version of Lowe's modification of Yahalom Protocol")
    print("10) Timed version of Paulson's modification of Yahalom Protocol")
    print("11) Timed version of BAN simplified version of Yahalom Protocol")
    print("12) Timed version of Woo Lam Pi Protocol")
    print("13) Timed version of Woo Lam Pi 1 Protocol")
    print("14) Timed version of Woo Lam Pi 2 Protocol")
    print("15) Timed version of Woo Lam Pi 3 Protocol")
    print("16) Timed version of Andrew Protocol")
    print("17) Timed version of Lowe's modification of Andrew Protocol")
    print("18) Timed version of Lowe's modification of Wide Mouthed Frog Protocol")
    print("19) MobInfoSec")
    print()
