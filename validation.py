def checkInts(min, max):
    try:
        result = int(input("Choose version: "))
        if result < min or result > max:
            print("You choose bad option")
            exit(1)
        return result
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)

def check1Lifetime():
    try:
        L1 = int(input("Choose L1: "))
        if L1 < 0:
            print("You choose bad lifetime")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    return L1


def check2Lifetimes():
    try:
        L1 = int(input("Choose L1: "))
        if L1 < 0:
            print("You choose bad lifetime")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        L2 = int(input("Choose L2: "))
        if L2 < 0:
            print("You choose bad lifetime")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    return L1, L2

def check3Lifetimes():
    try:
        L1 = int(input("Choose L1: "))
        if L1 < 0:
            print("You choose bad lifetime")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        L2 = int(input("Choose L2: "))
        if L2 < 0:
            print("You choose bad lifetime")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        L3 = int(input("Choose L3: "))
        if L3 < 0:
            print("You choose bad lifetime")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)

    return L1, L2, L3


def check4Lifetimes():
    try:
        L1 = int(input("Choose L1: "))
        if L1 < 0:
            print("You choose bad lifetime")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        L2 = int(input("Choose L2: "))
        if L2 < 0:
            print("You choose bad lifetime")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        L3 = int(input("Choose L3: "))
        if L3 < 0:
            print("You choose bad lifetime")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)

    try:
        L4 = int(input("Choose L4: "))
        if L4 < 0:
            print("You choose bad lifetime")
            exit(1)

    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)

    return L1, L2, L3, L4


def check3Delays():
    print("Please choose delays in the network:")
    try:
        D1 = int(input("Choose D1: "))
        if D1 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D2 = int(input("Choose D2: "))
        if D2 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D3 = int(input("Choose D3: "))
        if D3 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    return D1, D2, D3

def check2Delays():
    print("Please choose delays in the network:")
    try:
        D1 = int(input("Choose D1: "))
        if D1 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D2 = int(input("Choose D2: "))
        if D2 <1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    return D1, D2

def check4Delays():
    print("Please choose delays in the network:")
    try:
        D1 = int(input("Choose D1: "))
        if D1 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D2 = int(input("Choose D2: "))
        if D2 <1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D3 = int(input("Choose D3: "))
        if D3 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D4 = int(input("Choose D4: "))
        if D4 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)

    return D1, D2, D3, D4



def check5Delays():
    print("Please choose delays in the network:")
    try:
        D1 = int(input("Choose D1: "))
        if D1 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D2 = int(input("Choose D2: "))
        if D2 <1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D3 = int(input("Choose D3: "))
        if D3 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D4 = int(input("Choose D4: "))
        if D4 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D5 = int(input("Choose D5: "))
        if D5 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)

    return D1, D2, D3, D4, D5




def check6Delays():
    print("Please choose delays in the network:")
    try:
        D1 = int(input("Choose D1: "))
        if D1 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D2 = int(input("Choose D2: "))
        if D2 <1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D3 = int(input("Choose D3: "))
        if D3 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D4 = int(input("Choose D4: "))
        if D4 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D5 = int(input("Choose D5: "))
        if D5 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    try:
        D6 = int(input("Choose D6: "))
        if D6 < 1:
            print("You choose bad delay")
            exit(1)
    except ValueError:
        print("No valid integer! Please try again ...")
        exit(1)
    return D1, D2, D3, D4, D5, D6