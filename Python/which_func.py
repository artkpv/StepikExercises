"""
Вашей программе доступна переменная functions, в которой находится список функций.
Каждая функция принимает на вход один аргумент и возвращает некоторое значение или бросает исключение.

Вам необходимо найти в списке функций такую функцию, которая принимает на вход целое число xx, и возвращает целое число равное x2x2. Выведите номер этой функции в списке.
"""

def f0(x):
    return str(x)

def f1(x):
    return x * x

def f2(x):
    return [x] * x

def f3(x):
    raise AssertionError

def f4() :
    pass

def f5(x) :
    return f1(x)

functions = [f0, f2, f3, f4, f5, f1]

import inspect
checked = []
for i in range(len(functions)) :
    f = functions[i]
    r = None
    try :
        if type(f) not in checked and callable(f) :
            args = inspect.getargspec(f)
            if len(args.args) > 0 :
                r = f(i)
        checked.append(type(f))
    except BaseException :
        pass

    if type(r) == int and r == i*i :
        print(i)
        exit()



