import sys

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    f.close()
    val = get_val(lines)
    #print(val)
    nrComp, nrOfClocks, LL, k = get_param(val)
    print("nrComp =", nrComp, ", nrOfClocks =", nrOfClocks, ", LL =", LL, ", k =", k, "\n")
    print("m: (delta, (actions), (locations), (clocks), globaltime)")
    print()
    deltas = get_deltas(val, LL, k)
    actions = get_actions(val, nrComp, LL, k)
    locations = get_locations(val, nrComp, LL, k)
    clocks = get_clocks(val, nrOfClocks, LL, k)
    #print(clocks)
    global_time = get_global_time(val, LL, k)
    loops = get_loops(val, LL)
    create_paths(deltas, actions, locations, clocks, global_time, nrComp, nrOfClocks, LL, k, loops)

def get_val(lines):
    model = []
    for j in range(2, len(lines) - 1, 2):
        var = lines[j].split()[1]
        value = lines[j + 1].strip()[0:-1].strip("()")
        model.append(var + "_" + value)
    model = sorted(model)
    val = []
    for element in model:
        val.append(element.split("_"))
    return val

def get_param(val):
    nrComp = nrOfClocks = LL = k = 0
    for v in val:
        if v[0] == "w":
            if int(v[1]) > LL:
                LL = int(v[1])
            if int(v[2]) > k:
                k = int(v[2])
            if int(v[3]) > nrComp:
                nrComp = int(v[3])
        elif v[0] == "x":
            if int(v[1]) > LL:
                LL = int(v[1])
            if int(v[2]) > k:
                k = int(v[2])
            if int(v[3]) > nrOfClocks:
                nrOfClocks = int(v[3])
    nrComp += 1
    nrOfClocks += 1
    LL += 1
    return (nrComp, nrOfClocks, LL, k)

def get_actions(val, nrComp, LL, k):
    a = []
    for _ in range(LL):
        a.append([ [0 for i in range(nrComp + 1)] for j in range(k + 1)])
    for v in val:
        if v[0] == "a":
            a[int(v[1])][int(v[2])][int(v[3])] = int(v[4])
    return a

def get_locations(val, nrComp, LL, k):
    w = []
    for _ in range(LL):
        w.append([ [0 for i in range(nrComp + 1)] for j in range(k + 1)])
    for v in val:
        if v[0] == "w":
            w[int(v[1])][int(v[2])][int(v[3])] = int(v[4])
    return w

def prefix(s):
    s = s.split(" ")
    if len(s) == 3:
        s = s[1] + " " + s[0] + s[2]
    else:
        s = s[0]
    return round(float(eval(s)), 3)

def get_clocks(val, nrOfClocks, LL, k):
    x = []
    for _ in range(LL):
        x.append([ [0.0 for i in range(nrOfClocks)] for j in range(k + 1)])
    for v in val:
        if v[0] == "x":
            x[int(v[1])][int(v[2])][int(v[3])] = prefix(v[4])
    return x

def get_loops(val, LL):
    u = []
    for _ in range(LL):
        u.append(None)
    for v in val:
        if v[0] == "u":
            u[int(v[1])] = int(v[2])
    return u

def get_deltas(val, LL, k):
    t = []
    for _ in range(LL):
        t.append([0.0 for j in range(k + 1)])
    for v in val:
        if v[0] == "t":
            t[int(v[1])][int(v[2])] = prefix(v[3])
    return t

def get_global_time(val, LL, k):
    y = []
    for _ in range(LL):
        y.append([0.0 for j in range(k + k + 1)])
    for v in val:
        if v[0] == "y":
            y[int(v[1])][int(v[2])] = prefix(v[3])
    return y

def create_paths(deltas, actions, locations, clocks, global_time, nrComp, nrOfClocks, LL, k, loops):
    for path in range(LL):
        # print("Witness number:", path, "A loop:", loops)
        for depth in range(k + 1):
            print(depth, end = ": (")
        
            # delta
            print(deltas[path][depth], end = ", (")
        
            # actions
            for j in range(nrComp - 1):
                print(actions[path][depth][j], end = ",")
            print(actions[path][depth][nrComp - 1], end = "), (")
        
            # locations
            for j in range(nrComp - 1):
                print(locations[path][depth][j], end = ",")
            print(locations[path][depth][nrComp - 1], end = "), (")
        
            # clocks
            for j in range(nrOfClocks - 1):
                print(clocks[path][depth][j], end = ",")
            print(clocks[path][depth][nrOfClocks - 1], end = "), ")
    
            #print(str(global_time[path][depth]) + ")")
            print()

        print()
        #print(list(enumerate(global_time[path])), "\n")

if __name__ == "__main__":
    main()

