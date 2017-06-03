import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
passwords = """9XB8nsIqRfYeswC
4sEhUGLEZti9BiN
bDjmT0NcIW8nzhb
ZN6QQoMOO1ZQLUY
RVrF2qdMpoq6Lib
tnnX7HH3vJ9Hiji
C24TJYYkqekv40l
B2ropluPaMAitzE
DRezNUVnr2zC0CP
XCNmpTvvZb1n3mX
"""

for p in passwords.split('\n') :
    plain = "[nothing]"
    try :
        plain = simplecrypt.decrypt(p, encrypted)
    except :
        pass

    print('Pass:', p)
    print('Plain:')
    print(plain)
    print('==end==')
