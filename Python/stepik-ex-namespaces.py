n = int(input())

rootNS = {'global' : {} }

def create(ns, parent, currentNS = rootNS) :
    """
    create <namespace> <parent> –  создать новое пространство имен с именем
    <namespace> внутри пространства <parent>
    """
    #print('create(',ns,parent,currentNS,')')
    for key in currentNS :
        if parent == key :
            assert(type(currentNS[key]) is dict)
            currentNS[key][ns] = {}
            return
        elif type(currentNS[key]) is dict :
            create(ns, parent, currentNS[key])

def add(ns, var, currentNS = rootNS) :
    """
    add <namespace> <var> – добавить в пространство <namespace> переменную <var>
    """
    #print('add(',ns,var,currentNS,')')
    for key in currentNS :
        if key == ns :
            assert(type(currentNS[key]) is dict)
            currentNS[key][var] = 1
            return
        elif type(currentNS[key]) is dict  :
            add(ns, var, currentNS[key])

def get_ns(ns, currentNS = rootNS, path = [['global', rootNS['global']]]) :
    """
    traverses till NS is found building the path
    """
    #print('traverse(',ns,path,currentNS,')')

    for key in currentNS :
        if key == ns :
            path.append([key, currentNS[key]])
            return path

        if type(currentNS[key]) is dict :
            foundPath = get_ns(ns, currentNS[key], path + [[key, currentNS[key]]])
            if foundPath :
                return foundPath
    return None # NS not found here

def get(ns, var) :
    """
    get <namespace> <var> – получить имя пространства, из которого будет взята
    переменная <var> при запросе из пространства <namespace>, или None, если
    такого пространства не существует
    """
    #print('get(',ns,var,')')
    path = get_ns(ns)

    assert(path is not None)

    for i in range(len(path) - 1, 0, -1) :
        ns = path[i]
        if var in ns[1] :
            print(ns[0])
            return
    print('None')

while True:
    import sys
    line = sys.stdin.readline()
    if not line :
        break
    args = line.split()
    exec(args[0] + '("' + args[1] + '", "' + args[2] + '")')
    #print(repr(rootNS))



