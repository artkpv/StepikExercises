class ClassType :
    def __init__(self, name) :
        self.name = name
        self.ancestors = [self]

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

for i in range(q) :
    first, second = input().split()
    print('Yes' if classTypes[second].is_descendant_to(classTypes[first]) else 'No')

class A(A) :
    def __init__(self) :
        pass

