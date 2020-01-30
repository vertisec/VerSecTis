import os
import subprocess


def createBMCcommand(k, BIN, NET, FORM):
    BLOG = NET + "-bmc-k" + str(k) + ".log"
    cmd = "/usr/bin/time"
    cmd = cmd + " -o " + BLOG + " -f \"%M %U %S KB\" "
    cmd = cmd + BIN + "/smtreach4tis " +  NET + " "
    cmd = cmd + FORM
    cmd = cmd + " " + str(k) + " >| " + NET + "-bmc-k" + str(k) + ".out"
    print(createBMCcommand)
    return cmd


def executeBMCCommand(cmdBMC):
    try:
        subprocess.check_output(cmdBMC, shell=True)
    except subprocess.CalledProcessError as err:
        print("SMT4WTA failure")
        exit(2)


def createSMTZ3command(k, NET):
    SLOG = NET + "-smt-k" + str(k) + ".log"
    cmd = "/usr/bin/time -o " + SLOG + " -f \"%M %U %S KB\" z3 -smt2 "
    cmd = cmd + NET + "-k" + str(k) + ".smt > "
    cmd = cmd + NET + "-k" + str(k) + ".out"
    return cmd


def executeSMTCommand(cmdSMT):
    try:
        result = subprocess.check_output(cmdSMT, shell=True)
    except subprocess.CalledProcessError as err:
        return 3


def headCommand(NET, k):
    cmd = "head -1 " + NET + "-k" + str(k) + ".out"
    return cmd


def deleteSMTFile(NET, k):
    try:
        subprocess.check_output("rm -f " + NET + "-k" + str(k) + ".smt", shell=True)
    except subprocess.CalledProcessError as err:
        print("rm smt file failure")
        exit(5)


def headResult(headCmd):
    try:
        result = subprocess.check_output(headCmd, universal_newlines=True, shell=True)
        return result
    except subprocess.CalledProcessError as err:
        print("head failure")
        exit(4)


def bmcAlg(nameWithoutNta, BIN, efo, maxK):
    print("BMC is starting...")
    k = 0
    NET = nameWithoutNta
    FORM = efo
    while k <= maxK:
        cmdBMC = createBMCcommand(k, BIN, NET, FORM)
        executeBMCCommand(cmdBMC)
        print("Checking satisfiability ... ")
        cmdSMT = createSMTZ3command(k, NET)
        executeSMTCommand(cmdSMT)

        headRes = headResult(headCommand(NET, k))
        deleteSMTFile(NET, k)
        strRes = str(headRes).rstrip()

        if strRes == "sat":
            os.system('clear')
            print("SATISFIABLE!\n")
            print("The property is REACHABLE for k=" + str(k))
            print()
            #break
            return k
        elif strRes == "unsat":
            if k == maxK:
                print()
                print()
                print("UNSATISFIABLE! \n")
                return maxK
            else:
                print("UNSATISFIABLE! \n")
        else:
            print("UNKNOWN $E\n")

        k = k + 2
    return -1


def createRemoveCommand(nameWithoutNta):
    cmd = "rm " + nameWithoutNta + "*"
    #+ "*.out " + nameWithoutNta + "*.log " + nameWithoutNta + "*.lck "
    #cmd = cmd + nameWithoutNta + "*.nta "
    return cmd

def executeRemoveCommand(cmdRM):
    try:
        result = subprocess.check_output(cmdRM, shell = True)
    except subprocess.CalledProcessError as err:
        print("rm failure")
        exit(1)
