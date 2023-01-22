'''
a = 11 * 2 ** 2 - 13 / 4 + 7
print(a)

from sys import getsizeof
a = sys.getsizeof(3**9090001)/(1024*1024)
print(a)

a = 4 ** 4 ** 4
print(a)

def poss_add(a, b):
    return a + b
print(poss_add(5, -7))

def foo(a):
    return a // -11, a % -11 
print(foo(11))

def num_sum(a):
    if a == int(a):
        return a + a
    else:
        print('Это не целое число')
print(num_sum(10.1))

def num_sum(a):
    if isinstance(a, int) and not isinstance(a, bool):
        a_sum_num = str(abs(a))
        sum_ = 0
        for i in a_sum_num:
            sum_ += int(i)
        return sum_
    return 'Это не целое число'
print(num_sum(101))    
'''
def magic(*args, x):
    sum_ = 0
    for i in args:
        sum_ += i ** 2
    if sum_ % x == 0:
        return 'Волшебство случается'
    return 'Никакого волшебства'
print(magic(1,2,3, x = 2))
