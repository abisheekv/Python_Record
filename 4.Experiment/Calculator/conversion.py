def band(x, y):
    return int(x) & int(y)

def bor(x, y):
    return int(x) | int(y)

def bxor(x, y):
    return int(x) ^ int(y)

def bnot(x):
    return ~int(x)

def lshift(x, positions=2):
    return int(x) << positions

def rshift(x, positions=2):
    return int(x) >> positions

def binary(x):
    return bin(int(x))[2:]

def octal(x):
    return oct(int(x))[2:]

def hexadecimal(x):
    return hex(int(x))[2:]

def btodecimal(x):
    return int(x, 2)

def otodecimal(x):
    return int(x, 8)

def htodecimal(x):
    return int(x, 16)
