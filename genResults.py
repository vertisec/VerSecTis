def genResultsSMT(nameWithoutNta, k):
    fileNameWholeResults = nameWithoutNta + ".results"
    fileNameBmcResults = nameWithoutNta + ".resultsbmc"
    fileNameSmtResults = nameWithoutNta + ".resultssmt"

    for i in range (0, k+1, 2):
        fileNameBmc = nameWithoutNta + "-bmc-k" + str(k) + ".log"
        fin = open(fileNameBmc, 'r')
        line = fin.readline()
        fout = open(fileNameBmcResults, 'a')
        fout.write(line)
        foutwhole = open(fileNameWholeResults, 'a')
        foutwhole.write(line)
        fout.close()
        fin.close()

        filenameSmt = nameWithoutNta + "-smt-k" + str(k) + ".log"
        fin = open(filenameSmt, 'r')
        line = fin.readline()
        if line.startswith("Command"):
            line = fin.readline()
        fout = open(fileNameSmtResults, 'a')
        fout.write(line)
        foutwhole = open(fileNameWholeResults, 'a')
        foutwhole.write(line)
        fout.close()
        fin.close()
        foutwhole.close()


def sumResults(nameWithoutNta):
    fileNameWholeResults = nameWithoutNta + ".results"
    fileNameBmcResults = nameWithoutNta + ".resultsbmc"
    fileNameSmtResults = nameWithoutNta + ".resultssmt"

    bmcMem = 0
    bmcTime = 0
    smtTime = 0
    smtMem = 0
    maxMem = 0
    allTime = 0

    fin = open(fileNameBmcResults, 'r')
    for line1 in fin:
        line = line1.split()
        if int(line[0]) > bmcMem:
            bmcMem = int(line[0])
        bmcTime = bmcTime + float(line[1])
    fin.close()

    fin = open(fileNameSmtResults, 'r')
    for line1 in fin:
        line = line1.split()
        if int(line[0]) > smtMem:
            smtMem = int(line[0])
        smtTime = smtTime + float(line[1])
    fin.close()

    fin = open(fileNameWholeResults, 'r')
    for line1 in fin:
        line = line1.split()
        if int(line[0]) > maxMem:
            maxMem = int(line[0])
        allTime = allTime + float(line[1])
    fin.close()

    bmc = "{0:.2f} ".format(bmcTime) + "s\t"
    bmc = bmc +"\t{0:.2f} ".format(bmcMem / 1024.0) + "MB"

    smt = "{0:.2f} ".format(smtTime) + "s\t"
    smt = smt + "\t{0:.2f} ".format(smtMem / 1024.0) + "MB"

    all = "{0:.2f} ".format(allTime) + "s\t"
    all = all + "\t{0:.2f} ".format(maxMem / 1024.0) + "MB"

    return bmc, smt, all

