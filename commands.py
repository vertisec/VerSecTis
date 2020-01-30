import subprocess as sp

def executeCommandGenerateNtaFile(cmd, directory):
    try:
        out = sp.check_output(cmd, shell = True)
        print("Generating nta file succesfull. File with the network of automata and the formula are in " + directory)
    except sp.CalledProcessError as err:
        print("Generate nta file failure")
        exit(2)