class Students :
    def __init__(self) :
        self.d = {}
        self.index = 0

    def add(self, studentName, mark):
        # добавление оценки
        if studentName not in self.d :
            self.d[studentName] = []
        self.d[studentName].append(mark)

    def goodStudents(self):
        # запрос хороших студентов
        return iter(Students.Iterator(self.d))

    def __iter__(self):
        return self.goodStudents()


    class Iterator :

        def __init__(self, students) :
            self.d = {}
            for k in students :
                self.d[k] = students[k]

        def __iter__(self):
            self.iterator = iter(self.d)
            return self

        def __next__(self):
            while True :
                student = next(self.iterator)
                mean = sum(self.d[student]) / len(self.d[student])
                if mean > 4.0:
                    return student



s = Students()
s.add("Anton", 5)
s.add("Bogdan", 3)
s.add("Kostya", 4)
s.add("Anton", 4)
print(list(s.goodStudents())) # ['Anton']
# Kostya не является хорошим студентом, потому что его средний балл ровно 4
s.add("Bogdan", 5)
print(list(s.goodStudents())) # ['Anton']
# Bogdan также имеет средний балл ровно 4 здесь
s.add("Bogdan", 5)
print(list(s.goodStudents())) # ['Anton', 'Bogdan']

firstiter = s.goodStudents()
s.add('Another5er', 5)
print(list(firstiter))

s.add("Bogdan", 5)
