# python3
# -*- coding: utf8 -*-


class Numbers:
    def __init__(self):
        self.actions = {}

    def _add(self, list_, x):
        if x not in list_:
            list_.append(x)

    def _remove(self, list_, x):
        if x in list_:
            list_.remove(x)

    def add(self, x, t):
        # добавить число
        assert(t not in self.actions)
        self.actions[t] = (self._add, x)

    def remove(self, x, t):
        # удалить число
        assert(t not in self.actions)
        self.actions[t] = (self._remove, x)

    def query(self, t):
        # вернуть объект-генератор – результат запроса
        # print('querying for ' + str(t))
        list_ = []
        for k in sorted(self.actions.keys()):
            if k >= t:
                break
            action = self.actions[k]
            action[0](list_, action[1])
            # print(' ' + action[0].__name__ + ' ' + str(action[1]))
        return iter(list_)


numbers = Numbers()
add = numbers.add
remove = numbers.remove
query = numbers.query


add(1, 1)
add(2, 10)
print(query(15))  # 1, 2

# в момент 15 мы увидим число 1, добавленное в момент 1, и число 2, добавленное
# в момент 10
print(query(6))  # 1
# в момент 6 мы не увидим 2, поскольку оно было добавленно позднее

remove(2, 8)

print(query(14))  # 1, 2
# мы увидим 2, так как оно было добавлено в момент 10, а удалено в момент 8

remove(1, 3)
add(1, 5)  # 1 a 1, 3 r 1, 5 a 1, 8 r 2, 10 a 2,
print(query(2))  # 1
# 1 было добавлено, но еще не удалено

print(query(4))  # пустая последовательность
# 1 было добавлено и удалено

print(query(6))  # 1
# 1 было добавлено, удалено и снова добавлено


