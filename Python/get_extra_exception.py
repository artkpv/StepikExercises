# https://stepik.org/lesson/%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B8-%D0%B8-%D0%B8%D1%81%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D1%8F-24463/step/7?unit=undefined

class ClassType :
    def __init__(self, name) :
        self.name = name
        self.ancestors = []

    def add_ancestor(self, a) :
        assert(type(a) == ClassType)
        self.ancestors.append(a)

    def __eq__(self, other) :
        return self.name == other.name

    def __repr__(self) :
        return ' <ClassType name={}, ancestors={}> '.format(self.name, self.ancestors)

    def is_descendant_to(self, other) :
        for a in self.ancestors :
            if a == other :
                return True
            if a != self and a.is_descendant_to(other) :
                return True
        return False

classTypes = {}
n = int(input())
for i in range(n) :
    classDef = input().split(" ")
    name = classDef[0]
    if name not in classTypes :
        classTypes[name] = ClassType(name)
    classType = classTypes[name]

    for j in range(2, len(classDef)) :
        ancestorName = classDef[j]
        if ancestorName not in classTypes :
            classTypes[ancestorName] = ClassType(ancestorName)
        assert classTypes[ancestorName]
        classType.add_ancestor(classTypes[ancestorName])

q = int(input())
caught = []
extra = []
for i in range(q) :
    name = input()

    isCaught = False
    exceptionType = classTypes[name]
    for t in caught :
        caughtType = classTypes[t]
        if t == name or exceptionType.is_descendant_to(caughtType) :
            isCaught = True
            break

    if isCaught and name not in extra : extra.append(name)
    else : caught.append(name)

for n in extra:
    print(n)
