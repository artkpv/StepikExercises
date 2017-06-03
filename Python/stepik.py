def foo():
    raise ArithmeticError()

try:
    foo()
except BaseException as e :
    print(type(e).__name__)
