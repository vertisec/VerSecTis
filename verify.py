from smtbmc import createRemoveCommand, bmcAlg, executeRemoveCommand
from genNames import *
from genResults import genResultsSMT, sumResults
from protocols import *
from commands import executeCommandGenerateNtaFile

realpath = (os.path.dirname(os.path.realpath(__file__)))
BIN = realpath + "/bin"
PROT = realpath + "/protocols"


def attackVersion(prot):
    if prot == 1:
        #done after Sabina's answers
        attackVersion, D1, D2, D3, L1, L2,= nspkt()
        print("Timed version of Needham Schroeder Public Key Protocol")
        print("Version of the attack: " + str(attackVersion))
        print3D2L(D1, D2, D3, L1, L2)
        print()
        maxK = 28
        print("Generating input files")
        verify3D2L(prot, attackVersion, D1, D2, D3, L1, L2, maxK)

    elif prot == 2:
        #done after Sabina's answer
        manInTheMiddleVersion, D1, D2, L1, L2, L3 = wmft()
        print("Timed version of Wide Mouthed Frog Protocol")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print2D3L(D1, D2, L1, L2, L3)
        print()
        maxK = 100
        print("Generating input files")
        verify2D3L(prot, manInTheMiddleVersion, D1, D2, L1, L2, L3, maxK)

    elif prot == 3:
        #done
        manInTheMiddleVersion, D1, D2, D3, D4, L1 = denning()
        print("Timed version of Denning-Sacco Protocol")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print4D1L(D1, D2, D3, D4, L1)
        print()
        maxK = 100
        print("Generating input files")
        verify4D1L(prot, manInTheMiddleVersion, D1, D2, D3, D4, L1, maxK)

    elif prot == 4:
        #done
        manInTheMiddleVersion, D1, D2, D3, D4, D5, D6, L1, L2 = kaochow()
        print("Timed version of Kao-Chow Protocol")
        print("Be aware that there is no execution where attack is possible")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print6D2L(D1, D2, D3, D4, D5, D6, L1, L2)
        print()
        maxK = 100
        print("Generating input files")
        verify6D2L(prot, manInTheMiddleVersion, D1, D2, D3, D4, D5, D6, L1, L2, maxK)

    elif prot == 5:
        # done
        manInTheMiddleVersion, D1, D2, D3, D4, D5, D6, L1, L2 = cskip()
        print("Timed version of Carlsen's Secret Key Initiator Protocol")
        print("Be aware that there is no execution where attack is possible")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print6D2L(D1, D2, D3, D4, D5, D6, L1, L2)
        print()
        maxK = 100
        print("Generating input files")
        verify6D2L(prot, manInTheMiddleVersion, D1, D2, D3, D4, D5, D6, L1, L2, maxK)

    elif prot == 6:
        #done
        manInTheMiddleVersion, D1, D2, D3, D4, L1, L2 = nssk()
        print("Timed version of Needham Schroeder Symetric Key Protocol")
        print("Be aware that there is no execution where attack is possible")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print4D2L(D1, D2, D3, D4, L1, L2)
        #print("Maximum k = ??")
        print()
        maxK = 100
        print("Generating input files")
        verify4D2L(prot, manInTheMiddleVersion, D1, D2, D3, D4, L1, L2, maxK)

    elif prot == 7:
        #done
        manInTheMiddleVersion, D1, D2, D3, D4, D5, L1, L2 = yahalom()
        print("Timed version of Yahalom Protocol")
        print("Be aware that there is no execution where attack is possible")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print5D2L(D1, D2, D3, D4, D5, L1, L2)
        print()
        maxK = 100
        print("Generating input files")
        verify5D2L(prot, manInTheMiddleVersion, D1, D2, D3, D4, D5, L1, L2, maxK)

    elif prot == 8:
        #done
        attackVersion, D1, D2, D3, L1, L2,= nspktLowe()
        print("Timed version of the Lowe's modification of Needham Schroeder Public Key Protocol")
        print("Version of the attack: " + str(attackVersion))
        print3D2L(D1, D2, D3, L1, L2)
        print("Maximum k = 28")
        print()
        maxK = 28
        print("Generating input files")
        verify3D2L(prot, attackVersion, D1, D2, D3, L1, L2, maxK)

    elif prot == 9:
        #done
        manInTheMiddleVersion, D1, D2, D3, D4, L1, L2 = yahalomLowe()
        print("Be aware that there is no execution where attack is possible")
        print("Timed version of Lowe's modification of Yahalom Protocol")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print4D2L(D1, D2, D3, D4, L1, L2)
        print()
        maxK = 100
        print("Generating input files")
        verify4D2L(prot, manInTheMiddleVersion, D1, D2, D3, D4, L1, L2, maxK)

    elif prot == 10:
        #done
        manInTheMiddleVersion, D1, D2, D3, D4, L1, L2 = yahalomPaulson()
        print("Timed version of Paulson's modification of Yahalom Protocol")
        print("Be aware that there is no execution where attack is possible")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print4D2L(D1, D2, D3, D4, L1, L2)
        #print("Maximum k = ??")
        print()
        maxK = 100
        print("Generating input files")
        verify4D2L(prot, manInTheMiddleVersion, D1, D2, D3, D4, L1, L2, maxK)


    elif prot == 11:
        #done
        manInTheMiddleVersion, D1, D2, D3, D4, D5, L1, L2 = yahalomBAN()
        print("Timed version of BAN simplified version of Yahalom Protocol")
        print("Be aware that there is no execution where attack is possible")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print5D2L(D1, D2, D3, D4, D5, L1, L2)
        print()
        maxK = 100
        print("Generating input files")
        verify5D2L(prot, manInTheMiddleVersion, D1, D2, D3, D4, D5, L1, L2, maxK)

    elif prot == 12:
        #sprawdzone przez tate
        manInTheMiddleVersion, D1, D2, D3, L1, L2 = wooLamPi()
        print("Timed version of Woo Lam Pi Protocol")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print3D2L(D1, D2, D3, L1, L2)
        print()
        maxK = 100
        print("Generating input files")
        verify3D2L(prot, manInTheMiddleVersion, D1, D2, D3, L1, L2, maxK)

    elif prot == 13:
        # sprawdzone przez tate
        manInTheMiddleVersion, D1, D2, D3, L1, L2 = wooLamPi1()
        print("Timed version of Woo Lam Pi 1 Protocol")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print3D2L(D1, D2, D3, L1, L2)
        print()
        maxK = 100
        print("Generating input files")
        verify3D2L(prot, manInTheMiddleVersion, D1, D2, D3, L1, L2, maxK)


    elif prot == 14:
        # sprawdzone przez tate
        manInTheMiddleVersion, D1, D2, D3, L1, L2 = wooLamPi2()
        print("Timed version of Woo Lam Pi 2 Protocol")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print3D2L(D1, D2, D3, L1, L2)
        print()
        maxK = 100
        print("Generating input files")
        verify3D2L(prot, manInTheMiddleVersion, D1, D2, D3, L1, L2, maxK)

    elif prot == 15:
        # sprawdzone przez tate

        manInTheMiddleVersion, D1, D2, D3, L1, L2 = wooLamPi3()
        print("Timed version of Woo Lam Pi 3 Protocol")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print3D2L(D1, D2, D3, L1, L2)
        print()
        maxK = 100
        print("Generating input files")
        verify3D2L(prot, manInTheMiddleVersion, D1, D2, D3, L1, L2, maxK)

    elif prot == 16:
        # sprawdzone przez tate

        manInTheMiddleVersion, D1, D2, D3, D4, L1, L2 = andrew()
        print("Timed version of Andrew Protocol")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print4D2L(D1, D2, D3, D4, L1, L2)
        print()
        maxK = 100
        print("Generating input files")
        verify4D2L(prot, manInTheMiddleVersion, D1, D2, D3, D4, L1, L2, maxK)

    elif prot == 17:
        # sprawdzone przez tate

        manInTheMiddleVersion, D1, D2, D3, L1, L2 = andrewLowe()
        print("Timed version of Lowe's modification of Andrew Protocol")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print3D2L(D1, D2, D3, L1, L2)
        print()
        maxK = 100
        print("Generating input files")
        verify3D2L(prot, manInTheMiddleVersion, D1, D2, D3, L1, L2, maxK)

    elif prot == 18:
        manInTheMiddleVersion, D1, D2, D3, L1, L2, L3 = wmftLowe()
        print("Timed version of Lowe's modification of Wide Mouthed Frog Protocol")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print2D3L(D1, D2, D3, L1, L2)
        print("Maximum k = ??")
        print()
        maxK = 100
        print("Generating input files")
        verify3D3L(prot, manInTheMiddleVersion, D1, D2, D3, L1, L2, L3, maxK)

    elif prot == 19:
        manInTheMiddleVersion, D1, D2, D3, L1, L2, L3, L4 = mobinfosec()
        print("MobInfoSec")
        print("Version of the attack: Man in the Middle " + str(manInTheMiddleVersion))
        print3D4L(D1, D2, D3, L1, L2, L3, L4)
        print()
        maxK = 100
        print("Generating input files")
        verify3D4L(prot, manInTheMiddleVersion, D1, D2, D3, L1, L2, L3, L4, maxK)
    else:
        print("Not supported yet")





def verify3D2L(protocol, version, D1, D2, D3, L1, L2,  maxK):
    if protocol == 1:
        if version == 1 or version ==2:
            manInTheMiddle3D2L("nspkt", version, D1, D2, D3, L1, L2, maxK)
        elif version == 3 or version ==4:
            lowe3D2L("nspkt", version, D1, D2, D3, L1, L2, maxK)
    elif protocol == 8:
        if version == 1 or version == 2:
            manInTheMiddle3D2L("nspkLowe", version, D1, D2, D3, L1, L2, maxK)
    elif protocol == 12:
        manInTheMiddle3D2L("wooLamPi", version, D1, D2, D3, L1, L2, maxK)
    elif protocol == 13:
        manInTheMiddle3D2L("wooLamPi1", version, D1, D2, D3, L1, L2, maxK)
    elif protocol == 14:
        manInTheMiddle3D2L("wooLamPi2", version, D1, D2, D3, L1, L2, maxK)
    elif protocol == 15:
        manInTheMiddle3D2L("wooLamPi3", version, D1, D2, D3, L1, L2, maxK)
    elif protocol == 17:
        manInTheMiddle3D2L("andrewLowe", version, D1, D2, D3, L1, L2, maxK)



def verify3D4L(protocol, version, D1, D2, D3, L1, L2, L3, L4, maxK):
    if protocol == 19:
        manInTheMiddle3D4L("mobinfosec", version, D1, D2, D3, L1, L2, L3, L4, maxK)

def verify3D3L(protocol, version, D1, D2, D3, L1, L2, L3, maxK):
    if protocol == 18:
        manInTheMiddle3D3L("wmftLowe", version, D1, D2, D3, L1, L2, L3, maxK)


def verify2D3L(protocol, version, D1, D2, L1, L2, L3, maxK):
    if protocol == 2:
        manInTheMiddle2D3L("wmft", version, D1, D2, L1, L2, L3, maxK)

def verify4D1L(protocol, version, D1, D2, D3, D4, L1, maxK):
    if protocol == 3:
        manInTheMiddle4D1L("denning", version, D1, D2, D3, D4, L1, maxK)


def verify4D2L(protocol, version, D1, D2, D3, D4, L1, L2, maxK):
    if protocol == 6:
        manInTheMiddle4D2L("nssk", version, D1, D2, D3, D4, L1, L2, maxK)
    elif protocol == 9:
        manInTheMiddle4D2L("yahalomLowe", version, D1, D2, D3, D4, L1, L2, maxK)
    elif protocol == 10:
        manInTheMiddle4D2L("yahalomPaulson", version, D1, D2, D3, D4, L1, L2, maxK)
    elif protocol == 16:
        manInTheMiddle4D2L("andrew", version, D1, D2, D3, D4, L1, L2, maxK)

def verify5D2L(protocol, version, D1, D2, D3, D4, D5, L1, L2, maxK):
    if protocol == 7:
        manInTheMiddle5D2L("yahalom", version, D1, D2, D3, D4, D5, L1, L2, maxK)
    elif protocol == 11:
        manInTheMiddle5D2L("yahalomBAN", version, D1, D2, D3, D4, D5, L1, L2, maxK)


def verify6D2L(protocol, version, D1, D2, D3, D4, D5, D6, L1, L2, maxK):
    if protocol == 4:
        manInTheMiddle6D2L("kaochow1", version, D1, D2, D3, D4, D5, D6, L1, L2, maxK)
    if protocol == 5:
        manInTheMiddle6D2L("cskip", version, D1, D2, D3, D4, D5, D6, L1, L2, maxK)


def afterVerification(nameWithoutNta, k):
    genResultsSMT(nameWithoutNta, k)
    bmc, smt, all = sumResults(nameWithoutNta)
    executeRemoveCommand(createRemoveCommand(nameWithoutNta))
    print("BMC time \t BMC memory")
    print(bmc)
    print()
    print("Z3 time \t Z3 memory")
    print(smt)
    print()
    print("Time \t\t MAX memory")
    print(all)
    fopen = open(nameWithoutNta + ".dat", 'w')
    fopen.write("BMC time \t BMC memory\n")
    fopen.write(bmc + "\n\n")
    fopen.write("Z3 time \t Z3 memory\n")
    fopen.write(smt + "\n\n")
    fopen.write("Time \t\t MAX memory\n")
    fopen.write(all + "\n")
    fopen.close()
    print("\nResults saved in " + nameWithoutNta + ".dat")
    print()
    print()
    input("Press ENTER to continue")



def manInTheMiddle2D1L(protName, version, D1, D2, L1, maxK):
    if version == 1:
        name = PROT + "/" + protName + "/Man1/" + protName + "_Man1"
        directory = PROT + "/" + protName +"/Man1/"
        efo = directory + protName + "_Man1"
    if version == 2:
        name = PROT + "/" + protName + "/Man2/" + protName + "_Man2"
        directory = PROT + "/" + protName +"/Man2/"
        efo = directory + protName + "_Man2"
    cmd = generateNet2D1Lcommand(name, D1, D2, L1)
    executeCommandGenerateNtaFile(cmd, directory)
    nameWithoutNta = generateNameWithoutNta2D1L(name, D1, D2, L1)
    k = bmcAlg(nameWithoutNta, BIN, efo, maxK)
    afterVerification(nameWithoutNta, k)


def manInTheMiddle2D2L(protName, version, D1, D2, L1, L2, maxK):
    if version == 1:
        name = PROT + "/" + protName + "/Man1/" + protName + "_Man1"
        directory = PROT + "/" + protName +"/Man1/"
        efo = directory + protName + "_Man1"
    if version == 2:
        name = PROT + "/" + protName + "/Man2/" + protName + "_Man2"
        directory = PROT + "/" + protName +"/Man2/"
        efo = directory + protName + "_Man2"
    cmd = generateNet2D2Lcommand(name, D1, D2, L1, L2)
    executeCommandGenerateNtaFile(cmd, directory)
    nameWithoutNta = generateNameWithoutNta2D2L(name, D1, D2, L1, L2)
    k = bmcAlg(nameWithoutNta, BIN, efo, maxK)
    afterVerification(nameWithoutNta, k)

def manInTheMiddle3D2L(protName, version, D1, D2, D3, L1, L2, maxK):
    if version == 1:
        name = PROT + "/" + protName + "/Man1/" + protName + "_Man1"
        directory = PROT + "/" + protName +"/Man1/"
        efo = directory + protName + "_Man1"
    if version == 2:
        name = PROT + "/" + protName + "/Man2/" + protName + "_Man2"
        directory = PROT + "/" + protName +"/Man2/"
        efo = directory + protName + "_Man2"
    cmd = generateNet3D2Lcommand(name, D1, D2, D3, L1, L2)
    print(cmd)
    executeCommandGenerateNtaFile(cmd, directory)
    nameWithoutNta = generateNameWithoutNta3D2L(name, D1, D2, D3, L1, L2)
    k = bmcAlg(nameWithoutNta, BIN, efo, maxK)
    afterVerification(nameWithoutNta, k)


def manInTheMiddle2D3L(protName, version, D1, D2, L1, L2, L3, maxK):
    if version == 1:
        name = PROT + "/" + protName + "/Man1/" + protName + "_Man1"
        directory = PROT + "/" + protName +"/Man1/"
        efo = directory + protName + "_Man1"
    if version == 2:
        name = PROT + "/" + protName + "/Man2/" + protName + "_Man2"
        directory = PROT + "/" + protName +"/Man2/"
        efo = directory + protName + "_Man2"
    cmd = generateNet2D3Lcommand(name, D1, D2, L1, L2, L3)
    print(cmd)
    executeCommandGenerateNtaFile(cmd, directory)
    nameWithoutNta = generateNameWithoutNta2D3L(name, D1, D2, L1, L2, L3)
    k = bmcAlg(nameWithoutNta, BIN, efo, maxK)
    afterVerification(nameWithoutNta, k)

def lowe3D2L(protName, version, D1, D2, D3, L1, L2, maxK):
    if version == 3:
        name = PROT + "/" + protName + "/Lowe1/" + protName + "_Lowe1"
        directory = PROT + "/" + protName +"/Lowe1/"
        efo = directory + protName + "_Lowe1"
    if version == 4:
        name = PROT + "/" + protName + "/Lowe2/" + protName + "_Lowe2"
        directory = PROT + "/" + protName +"/Lowe2/"
        efo = directory + protName + "_Lowe2"
    cmd = generateNet3D2Lcommand(name, D1, D2, D3, L1, L2)
    print(cmd)
    executeCommandGenerateNtaFile(cmd, directory)
    nameWithoutNta = generateNameWithoutNta3D2L(name, D1, D2, D3, L1, L2)
    k = bmcAlg(nameWithoutNta, BIN, efo, maxK)
    afterVerification(nameWithoutNta, k)

def manInTheMiddle4D1L(protName, version, D1, D2, D3, D4, L1, maxK):
    if version == 1:
        name = PROT + "/" + protName + "/Man1/" + protName + "_Man1"
        directory = PROT + "/" + protName +"/Man1/"
        efo = directory + protName + "_Man1"
    if version == 2:
        name = PROT + "/" + protName + "/Man2/" + protName + "_Man2"
        directory = PROT + "/" + protName +"/Man2/"
        efo = directory + protName + "_Man2"
    cmd = generateNet4D1Lcommand(name, D1, D2, D3, D4, L1)
    print(cmd)
    executeCommandGenerateNtaFile(cmd, directory)
    nameWithoutNta = generateNameWithoutNta4D1L(name, D1, D2, D3, D4, L1)
    k = bmcAlg(nameWithoutNta, BIN, efo, maxK)
    afterVerification(nameWithoutNta, k)



def manInTheMiddle4D2L(protName, version, D1, D2, D3, D4, L1, L2, maxK):
    if version == 1:
        name = PROT + "/" + protName + "/Man1/" + protName + "_Man1"
        directory = PROT + "/" + protName +"/Man1/"
        efo = directory + protName + "_Man1"
    if version == 2:
        name = PROT + "/" + protName + "/Man2/" + protName + "_Man2"
        directory = PROT + "/" + protName +"/Man2/"
        efo = directory + protName + "_Man2"
    cmd = generateNet4D2Lcommand(name, D1, D2, D3, D4, L1, L2)
    print(cmd)
    executeCommandGenerateNtaFile(cmd, directory)
    nameWithoutNta = generateNameWithoutNta4D2L(name, D1, D2, D3, D4, L1, L2)
    k = bmcAlg(nameWithoutNta, BIN, efo, maxK)
    afterVerification(nameWithoutNta, k)


def manInTheMiddle5D2L(protName, version, D1, D2, D3, D4, D5, L1, L2, maxK):
    if version == 1:
        name = PROT + "/" + protName + "/Man1/" + protName + "_Man1"
        directory = PROT + "/" + protName +"/Man1/"
        efo = directory + protName + "_Man1"
    if version == 2:
        name = PROT + "/" + protName + "/Man2/" + protName + "_Man2"
        directory = PROT + "/" + protName +"/Man2/"
        efo = directory + protName + "_Man2"
    cmd = generateNet5D2Lcommand(name, D1, D2, D3, D4, D5, L1, L2)
    print(cmd)
    executeCommandGenerateNtaFile(cmd, directory)
    nameWithoutNta = generateNameWithoutNta5D2L(name, D1, D2, D3, D4, D5, L1, L2)
    k = bmcAlg(nameWithoutNta, BIN, efo, maxK)
    afterVerification(nameWithoutNta, k)

def manInTheMiddle6D2L(protName, version, D1, D2, D3, D4, D5, D6, L1, L2, maxK):
    if version == 1:
        name = PROT + "/" + protName + "/Man1/" + protName + "_Man1"
        directory = PROT + "/" + protName +"/Man1/"
        efo = directory + protName + "_Man1"
    if version == 2:
        name = PROT + "/" + protName + "/Man2/" + protName + "_Man2"
        directory = PROT + "/" + protName +"/Man2/"
        efo = directory + protName + "_Man2"
    cmd = generateNet6D2Lcommand(name, D1, D2, D3, D4, D5, D6, L1, L2)
    print(cmd)
    executeCommandGenerateNtaFile(cmd, directory)
    nameWithoutNta = generateNameWithoutNta6D2L(name, D1, D2, D3, D4, D5, D6, L1, L2)
    k = bmcAlg(nameWithoutNta, BIN, efo, maxK)
    afterVerification(nameWithoutNta, k)

def manInTheMiddle3D4L(protName, version, D1, D2, D3, L1, L2, L3, L4, maxK):
    if version == 1:
        name = PROT + "/" + protName + "/Man1/" + protName + "_Man1"
        directory = PROT + "/" + protName +"/Man1/"
        efo = directory + protName + "_Man1"
    if version == 2:
        name = PROT + "/" + protName + "/Man2/" + protName + "_Man2"
        directory = PROT + "/" + protName +"/Man2/"
        efo = directory + protName + "_Man2"
    if version == 3:
        name = PROT + "/" + protName + "/Man3/" + protName + "_Man3"
        directory = PROT + "/" + protName + "/Man3/"
        efo = directory + protName + "_Man3"
    if version == 4:
        name = PROT + "/" + protName + "/Man4/" + protName + "_Man4"
        directory = PROT + "/" + protName + "/Man4/"
        efo = directory + protName + "_Man4"

    cmd = generateNet3D4Lcommand(name, D1, D2, D3, L1, L2, L3, L4)
    print(cmd)
    executeCommandGenerateNtaFile(cmd, directory)
    nameWithoutNta = generateNameWithoutNta3D4L(name, D1, D2, D3, L1, L2, L3, L4)
    k = bmcAlg(nameWithoutNta, BIN, efo, maxK)
    afterVerification(nameWithoutNta, k)



def manInTheMiddle3D3L(protName, version, D1, D2, D3, L1, L2, L3, maxK):
    if version == 1:
        name = PROT + "/" + protName + "/Man1/" + protName + "_Man1"
        directory = PROT + "/" + protName +"/Man1/"
        efo = directory + protName + "_Man1"
    if version == 2:
        name = PROT + "/" + protName + "/Man2/" + protName + "_Man2"
        directory = PROT + "/" + protName +"/Man2/"
        efo = directory + protName + "_Man2"

    cmd = generateNet3D3Lcommand(name, D1, D2, D3, L1, L2, L3)
    print(cmd)
    executeCommandGenerateNtaFile(cmd, directory)
    nameWithoutNta = generateNameWithoutNta3D3L(name, D1, D2, D3, L1, L2, L3)
    k = bmcAlg(nameWithoutNta, BIN, efo, maxK)
    afterVerification(nameWithoutNta, k)


def print2D1L(D1, D2, L1):
    print("Delays:")
    print("D1 = " + str(D1))
    print("D2 = " + str(D2))
    print("Lifetime:")
    print("L1 = " + str(L1))

def print2D2L(D1, D2, L1, L2):
    print("Delays:")
    print("D1 = " + str(D1))
    print("D2 = " + str(D2))
    print("Lifetimes:")
    print("L1 = " + str(L1))
    print("L2 = " + str(L2))

def print3D2L(D1, D2, D3, L1, L2):
    print("Delays:")
    print("D1 = " + str(D1))
    print("D2 = " + str(D2))
    print("D3 = " + str(D3))
    print("Lifetimes:")
    print("L1 = " + str(L1))
    print("L2 = " + str(L2))

def print3D4L(D1, D2, D3, L1, L2, L3, L4):
    print("Delays:")
    print("D1 = " + str(D1))
    print("D2 = " + str(D2))
    print("D3 = " + str(D3))
    print("Lifetimes:")
    print("L1 = " + str(L1))
    print("L2 = " + str(L2))
    print("L3 = " + str(L3))
    print("L4 = " + str(L4))

def print2D3L(D1, D2, L1, L2, L3):
    print("Delays:")
    print("D1 = " + str(D1))
    print("D2 = " + str(D2))
    print("Lifetimes:")
    print("L1 = " + str(L1))
    print("L2 = " + str(L2))
    print("L3 = " + str(L3))

def print4D1L(D1, D2, D3, D4, L1):
    print("Delays:")
    print("D1 = " + str(D1))
    print("D2 = " + str(D2))
    print("D3 = " + str(D3))
    print("D4 = " + str(D4))
    print("Lifetime:")
    print("L1 = " + str(L1))

def print4D2L(D1, D2, D3, D4, L1, L2):
    print("Delays:")
    print("D1 = " + str(D1))
    print("D2 = " + str(D2))
    print("D3 = " + str(D3))
    print("D4 = " + str(D4))
    print("Lifetimes:")
    print("L1 = " + str(L1))
    print("L2 = " + str(L2))

def print5D2L(D1, D2, D3, D4, D5, L1, L2):
    print("Delays:")
    print("D1 = " + str(D1))
    print("D2 = " + str(D2))
    print("D3 = " + str(D3))
    print("D4 = " + str(D4))
    print("D5 = " + str(D5))
    print("Lifetimes:")
    print("L1 = " + str(L1))
    print("L2 = " + str(L2))


def print6D2L(D1, D2, D3, D4, D5, D6, L1, L2):
    print("Delays:")
    print("D1 = " + str(D1))
    print("D2 = " + str(D2))
    print("D3 = " + str(D3))
    print("D4 = " + str(D4))
    print("D5 = " + str(D5))
    print("D6 = " + str(D6))
    print("Lifetimes:")
    print("L1 = " + str(L1))
    print("L2 = " + str(L2))


