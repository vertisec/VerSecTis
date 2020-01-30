from validation import checkInts, check3Delays, check2Lifetimes, check2Delays, check3Lifetimes, check1Lifetime, check4Delays, check6Delays, check5Delays, check4Lifetimes
import os

def nspkt():
    os.system('clear')
    print("Alice-Bob notation of Timed version of Needham Schroeder Public Key Protocol")
    print("1. A\t->\tB\t:\t{Ta ,A}Kb")
    print("2. B\t->\tA\t:\t{Ta, Tb}Ka")
    print("3. A\t->\tB\t:\t{Tb}Kb")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    print("3) Lowe 1")
    print("4) Lowe 2")
    manInTheMiddleVersion = checkInts(1, 4)
    if manInTheMiddleVersion == 1:
        print("Man in the Middle 1")
        print("An attack exists if:")
        print("L1 >= D2 + 1")
        print("L2 >= 3 * D2 + 1")
    elif manInTheMiddleVersion == 2:
        print("Man in the Middle 2")
        print("An attack exists if:")
        print("L1 >= 3 * D2 + 1")
        print("L2 >= D2 + 1")
    elif manInTheMiddleVersion == 3:
        print("Lowe 1")
        print("An attack exists if:")
        print("L1 >= 3 * D2 + 1")
        print("L2 >= D1 + 2 * D2 + 1")
    elif manInTheMiddleVersion == 4:
        print("Lowe 2")
        print("An attack exists if:")
        print("L1 >= D1 + 2 * D2 + 1")
        print("L2 >=  3 * D2 + 1")
    D1, D2, D3 = check3Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, L1, L2

def wmft():
    os.system('clear')
    print("Alice-Bob notation of Timed version of Wide Mouth Frog Protocol")
    print("1. A\t->\tS\t:\tA, {Ta, B, Kab}Kas")
    print("2. S\t->\tB\t:\t{Ts, A, Kab}Kbs")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)
    print("An attack does not exist")

    D1, D2 = check2Delays()
    L1, L2, L3 = check3Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, L1, L2, L3


def denning():
    os.system('clear')
    print("Alice-Bob notation of Denning-Sacco Protocol")

    print("1. A\t->\tS\t:\tA, B")
    print("2. S\t->\tA\t:\t{B, Kab, Ts, {Kab, A, Ts}Kbs}Kas")
    print("3. A\t->\tB\t:\t{Kab, A, Ts}Kbs")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)
    if manInTheMiddleVersion == 1:
        print("Man in the Middle 1")
        print("An attack exists if:")
        print("L1 >= D1 + D4 + 1")
    elif manInTheMiddleVersion == 2:
        print("Man in the Middle 2")
        print("An attack exists if:")
        print("L1 >= D1 + D4 + 1")
    D1, D2, D3, D4 = check4Delays()
    L1 = check1Lifetime()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, D4, L1

def kaochow():
    os.system('clear')
    print("Alice-Bob notation of Kao Chow 1 Protocol")
    print("1. A\t->\tS\t:\tA, B, Ta")
    print("2. S\t->\tB\t:\t{A, B, Ta, Kab}Kas, {A, B, Ta, Kab}Kbs")
    print("3. B\t->\tA\t:\t{A, B, Ta, Kab}Kas, {Ta}Kab, Tb")
    print("4. A\t->\tB\t:\t{Tb}Kab")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)
    print("An attack does not exist")

    D1, D2, D3, D4, D5, D6 = check6Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, D4, D5, D6, L1, L2

def cskip():
    os.system('clear')
    print("Alice-Bob notation of Carlsen's Secret Key Initiator Protocol")
    print("1. A\t->\tS\t:\tA, B, Ta")
    print("2. S\t->\tB\t:\t{A, B, Ta, Kab}Kas, {A, B, Ta, Kab}Kbs")
    print("3. B\t->\tA\t:\t{A, B, Ta, Kab}Kas, {Ta}Kab, Tb")
    print("4. A\t->\tB\t:\t{Tb}Kab")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)
    print("An attack does not exist")

    D1, D2, D3, D4, D5, D6 = check6Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, D4, D5, D6, L1, L2



def nssk():
    os.system('clear')
    print("Alice-Bob notation of Timed version of  Needham Schroeder Symetric Key Protocol")
    print("1. A\t->\tS\t:\tA, B, Ta")
    print("2. S\t->\tB\t:\t{Ta, B, Kab, {Kab, A}Kbs}Kas")
    print("3. A\t->\tB\t:\t{Kab ,A}Kbs")
    print("4. B\t->\tA\t:\t{Tb}Kab")
    print("5. A\t->\tB\t:\t{Tb}Kab")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)
    print("An attack does not exist")

    D1, D2, D3, D4 = check4Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, D4, L1, L2



def yahalom():
    os.system('clear')
    print("Alice-Bob notation of Yahalom Protocol")
    print("1. A\t->\tB\t:\tA, Ta")
    print("2. B\t->\tS\t:\tB, {A, Ta, Tb}Kbs")
    print("3. S\t->\tA\t:\t{B, Kab, Ta, Tb}Kas, {A, Kab}Kbs")
    print("4. A\t->\tB\t:\t{A, Kab}Kbs, {Tb}Kab")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)

    print("An attack does not exist")

    D1, D2, D3, D4, D5 = check5Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, D4, D5, L1, L2

def nspktLowe():
    os.system('clear')
    print("Alice-Bob notation Timed version of the Lowe's modification of Needham Schroeder Public Key Protocol")
    print("1. A\t->\tB\t:\t{Ta ,A}Kb")
    print("2. B\t->\tA\t:\t{Ta, Tb, B}Ka")
    print("3. A\t->\tB\t:\t{Tb}Kb")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)
    if manInTheMiddleVersion == 1:
        print("Man in the Middle 1")
        print("An attack exists if:")
        print("L1 >= 3 * D2 + 1")
        print("L2 >= D1 + 2 * D2 + 1")
    elif manInTheMiddleVersion == 2:
        print("Man in the Middle 2")
        print("An attack exists if:")
        print("L1 >= D1 + 2 * D2 + 1")
        print("L2 >= 3 * D2 + 1")
    D1, D2, D3 = check3Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, L1, L2

def yahalomLowe():
    os.system('clear')
    print("Alice-Bob notation of Timed version of Lowe's modification of Yahalom Protocol")
    print("1. A\t->\tB\t:\tA, Ta")
    print("2. B\t->\tS\t:\tB, {A, Ta, Tb}Kbs")
    print("3. S\t->\tA\t:\t{B, Kab, Ta, Tb}Kas")
    print("4. S\t->\tB\t:\t{A, Kab}Kbs")
    print("5. A\t->\tB\t:\t{A, B, S, Tb}Kab")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)
    print("An attack does not exist")

    D1, D2, D3, D4 = check4Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, D4, L1, L2

def yahalomPaulson():
    os.system('clear')
    print("Alice-Bob notation of Timed version of Paulson's modification of Yahalom Protocol")
    print("1. A\t->\tB\t:\tA, Ta")
    print("2. B\t->\tS\t:\tB, Tb, {A, Ta}Kbs")
    print("3. S\t->\tA\t:\tTb, {B, Kab, Ta}Kas, {A, B, Kab, Tb}Kbs")
    print("4. S\t->\tB\t:\t{A, B, Kab, Tb}Kbs, {Tb}Kab")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)
    print("An attack does not exist")

    D1, D2, D3, D4 = check4Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, D4, L1, L2

def yahalomBAN():
    os.system('clear')
    print("Alice-Bob notation of Timed version of BAN simplified version of Yahalom Protocol")
    print("1. A\t->\tB\t:\tA, Ta")
    print("2. B\t->\tS\t:\tB, Tb, {A, Ta}Kbs")
    print("3. S\t->\tA\t:\tTb, {B, Kab, Ta}Kas, {A, Kab, Tb}Kbs")
    print("4. A\t->\tB\t:\t{A, Kab, Tb}Kbs, {Tb}Kab")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)
    print("An attack does not exist")

    D1, D2, D3, D4, D5 = check5Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, D4, D5, L1, L2

def wooLamPi():
    os.system('clear')
    print("Alice-Bob notation of Timed version of Woo and Lam Pi Protocol")
    print("1. A\t->\tB\t:\tA")
    print("2. B\t->\tA\t:\tTb")
    print("3. A\t->\tB\t:\t{Tb}Kas")
    print("4. B\t->\tS\t:\t{A, {Tb}Kas}Kbs")
    print("5. S\t->\tB\t:\t{Tb}Kbs")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)
    if manInTheMiddleVersion == 1:
        print("Man in the Middle 1")
        print("An attack exists if:")
        print("L1 >= 0")
        print("L2 >= D2 + 2 * D3 + 1")

    elif manInTheMiddleVersion == 2:
        print("Man in the Middle 2")
        print("An attack exists if:")
        print("L1 >= D2 + 2 * D3 + 1")
        print("L2 >= 0")
    D1, D2, D3 = check3Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, L1, L2

def wooLamPi1():
    os.system('clear')
    print("Alice-Bob notation of Timed version of Woo and Lam Pi 1 Protocol")
    print("1. A\t->\tB\t:\tA")
    print("2. B\t->\tA\t:\tTb")
    print("3. A\t->\tB\t:\t{A, B, Tb}Kas")
    print("4. B\t->\tS\t:\t{A, B, {A, B, Tb}Kas}Kbs")
    print("5. S\t->\tB\t:\t{A, B, Tb}Kbs")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)

    if manInTheMiddleVersion == 1:
        print("Man in the Middle 1")
        print("An attack exists if:")
        print("L1 >= D2 + 2 * D3 + 1")
        print("L2 >= 0")
    elif manInTheMiddleVersion == 2:
        print("Man in the Middle 2")
        print("An attack exists if:")
        print("L1 >= 0")
        print("L2 >= D2 + 2 * D3 + 1")



    D1, D2, D3 = check3Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, L1, L2

def wooLamPi2():
    os.system('clear')
    print("Alice-Bob notation of Timed version of Woo and Lam Pi 2 Protocol")
    print("1. A\t->\tB\t:\tA")
    print("2. B\t->\tA\t:\tTb")
    print("3. A\t->\tB\t:\t{A, Tb}Kas")
    print("4. B\t->\tS\t:\t{A, {A, Tb}Kas}Kbs")
    print("5. S\t->\tB\t:\t{A, Tb}Kbs")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)

    if manInTheMiddleVersion == 1:
        print("Man in the Middle 1")
        print("An attack exists if:")
        print("L1 >= D2 + 2 * D3 + 1")
        print("L2 >= 0")
    elif manInTheMiddleVersion == 2:
        print("Man in the Middle 2")
        print("An attack exists if:")
        print("L1 >= 0")
        print("L2 >= D2 + 2 * D3 + 1")

    D1, D2, D3 = check3Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, L1, L2

def wooLamPi3():
    os.system('clear')
    print("Alice-Bob notation of Timed version of Woo and Lam Pi 3 Protocol")
    print("1. A\t->\tB\t:\tA")
    print("2. B\t->\tA\t:\tTb")
    print("3. A\t->\tB\t:\t{A, Tb}Kas")
    print("4. B\t->\tS\t:\t{A, {Tb}Kas}Kbs")
    print("5. S\t->\tB\t:\t{A, Tb}Kbs")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)

    if manInTheMiddleVersion == 1:
        print("Man in the Middle 1")
        print("An attack exists if:")
        print("L1 >= D2 + 2 * D3 + 1")
        print("L2 >= 0")
    elif manInTheMiddleVersion == 2:
        print("Man in the Middle 2")
        print("An attack exists if:")
        print("L1 >= 0")
        print("L2 >= D2 + 2 * D3 + 1")

    D1, D2, D3 = check3Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, L1, L2

def andrew():
    os.system('clear')
    print("Alice-Bob notation of Andrew Protocol")
    print("1. A\t->\tB\t:\tA, {Ta}Kab")
    print("2. B\t->\tA\t:\t{Ta, Tb}Kab")
    print("3. A\t->\tB\t:\t{Tb}Kab")
    print("4. B\t->\tA\t:\t{K'ab, T'b}Kab")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)

    if manInTheMiddleVersion == 1:
        print("Man in the Middle 1")
        print("An attack exists if:")
        print("L1 >= 0")
        print("L2 >= max(3 * D3, D4) + 1")
    elif manInTheMiddleVersion == 2:
        print("Man in the Middle 2")
        print("An attack exists if:")
        print("L1 >= 0")
        print("L2 >= 3 * D3 + 1, for D3 <= D4")
        print("L2 >= 2 * D3 + D4 + 1, for D3 > D4")


    D1, D2, D3, D4 = check4Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, D4, L1, L2

def andrewLowe():
    os.system('clear')
    print("Alice-Bob notation of Andrew Protocol")
    print("1. A\t->\tB\t:\tA, {Ta}Kab")
    print("2. B\t->\tA\t:\t{Ta, Tb}Kab")
    print("3. A\t->\tB\t:\t{Tb}Kab")
    print("4. B\t->\tA\t:\t{K'ab, T'b, Ta}Kab")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)

    if manInTheMiddleVersion == 1:
        print("Man in the Middle 1")
        print("An attack exists if:")
        print("For D2 <= D3:")
        print("L1 >= D2 + D3 + 1")
        print("L2 >= D2 + D3 + 1")
        print()
        print("For D2 > D3:")
        print("L1 >= 2 * D2 + 1")
        print("L2 >= D2 + D3 + 1")
    elif manInTheMiddleVersion == 2:
        print("Man in the Middle 2")
        print("An attack exists if:")
        print("For D2 <= D3:")
        print("L1 >= D2 + D3 + 1")
        print("L2 >= D2 + D3 + 1")
        print()
        print("For D2 > D3:")
        print("L1 >= D2 + D3 + 1")
        print("L2 >= 2 * D2 + 1")

    D1, D2, D3 = check3Delays()
    L1, L2 = check2Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, L1, L2


def wmftLowe():
    os.system('clear')
    print("Alice-Bob notation of Timed version of Lowe's modification of Wide Mouth Frog Protocol")
    print("1. A\t->\tS\t:\tA, {Ta, B, Kab}Kas")
    print("2. S\t->\tB\t:\t{Ts, A, Kab}Kbs")
    print("3. B\t->\tA\t:\t{Tb}Kab")
    print("2. A\t->\tB\t:\t{Tb}Kab")
    print()
    print("An attack does not exist")
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    manInTheMiddleVersion = checkInts(1, 2)

    D1, D2, D3 = check3Delays()
    L1, L2, L3 = check3Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, L1, L2, L3

def mobinfosec():
    os.system('clear')
    print("Alice-Bob notation of MobInfoSec")
    print("1. SP.A\t->\tMU.A\t:\tTsp.a, SP.A")
    print("2. MU.A\t->\tMU.B\t:\tTsp.a, SP.A")
    print("3. MU.B\t->\tSP.B\t:\tTsp.a, SP.A")
    print("4. SP.B\t->\tMU.B\t:\t{{Tsp.a, -Ksp.a, h(Tsp.b,Tsp.a,SP.A)}-Ksp.b}+Ksp.a")
    print("5. MU.B\t->\tMU.A\t:\t{{Tsp.a, -Ksp.a, h(Tsp.b,Tsp.a,SP.A)}-Ksp.b}+Ksp.a")
    print("6. MU.A\t->\tSP.A\t:\t{{Tsp.a, -Ksp.a, h(Tsp.b,Tsp.a,SP.A)}-Ksp.b}+Ksp.a")
    print()
    print("Versions of an attack")
    print("1) Man in the Middle 1")
    print("2) Man in the Middle 2")
    print("3) Man in the Middle 3")
    print("4) Man in the Middle 4")
    manInTheMiddleVersion = checkInts(1, 4)

    D1, D2, D3 = check3Delays()
    L1, L2, L3, L4 = check4Lifetimes()

    print("All the parameters have been chosen!")
    print("Press ENTER to verify")
    input()
    os.system('clear')
    return manInTheMiddleVersion, D1, D2, D3, L1, L2, L3, L4

