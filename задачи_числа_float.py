'''
a = 10.0 + 3 + 4
print(type(a))

def to_float(num):
    if isinstance(num, (int, float)):
        return float(num)
    return 'Невозможно преобразовать'
print(to_float(False))

def avg_5(a, b, c, d):
    return round((a + b + c + d) / 4, 5)
print(avg_5(2, 3.3, -5, 3.14))

def to_int(a, b):
    res = a * b
    if float(res).is_integer():
        return int(res)
    return res
print(to_int(2, 2.35)) 

from math import pi
def radius(V):
    return ((3 * V / (4 * pi)) ** (1/3))
print(radius(36))

def round_standart(num):
    if float(num):
        return round(num)
    return int(num)
print(round_standart(4.5))

def round_standart(num):
    if float(num):
        if num >= 0:
            return round(num + 0.05)
        else:
            return round(num - 0.05)
    return int(num)
print(round_standart(-4.96))

def round_standart(num):
    if num >= 0:
        sign = 1
    else:
        sign = -1
    return sign * int(abs(num) + 0.05)
print(round_standart(-4.97))
'''
def eqv(a, b, c):
    if abs(c - a - b) <= 0.01 * max(abs(a), abs(b)):
        return True
    return False
print(eqv(0.12, 0.31, 0.43))



    
