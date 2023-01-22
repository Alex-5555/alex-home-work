from pprint import pprint
'''
a = dict.fromkeys(['clubs-6', 'heart-6', 'diamond-6', 'spade-6'], 6)
b = dict.fromkeys(['clubs-7', 'heart-7', 'diamond-7', 'spade-7'], 7)
c = dict.fromkeys(['clubs-8', 'heart-8', 'diamond-8', 'spade-8'], 8)
d = dict.fromkeys(['clubs-9', 'heart-9', 'diamond-9', 'spade-9'], 9)
e = dict.fromkeys(['clubs-10', 'heart-10', 'diamond-10', 'spade-10'], 10)
f = dict.fromkeys(['clubs-J', 'heart-J', 'diamond-J', 'spade-J'], 3)
g = dict.fromkeys(['clubs-Q', 'heart-Q', 'diamond-Q', 'spade-Q'], 4)
h = dict.fromkeys(['clubs-K', 'heart-K', 'diamond-K', 'spade-K'], 5)
k = dict.fromkeys(['clubs-A', 'heart-A', 'diamond-A', 'spade-A'], 11)
a['friends'] = [{"name": "Dima"}, {"name": "Alex"}]
pprint(a)

# функция season, принимающая 1 аргумент — номер месяца 
# (от 1 до 12), и возвращающыя время года:
def season(a):
    if  1 <= a < 3 or a == 12:
        return 'winter'
    if  3 <= a < 6:
        return 'spring'
    if  6 <= a < 9:
        return 'summer'
    if  9 <= a < 12:
        return 'autumn'
    else:
        return 'wrong month number'
print(season(3))

# функция square, принимающая 1 аргумент — сторону квадрата, 
# и возвращающая 3 значения (с помощью кортежа): 
# периметр квадрата, площадь квадрата и диагональ квадрата.
def square(x):
    return x*4, x*2, x**2 + x**2
print(square(4))

# Написать функцию arithmetic, принимающую 3 аргумента: 
# первые 2 - числа, третий - операция, которая должна быть 
# произведена над ними. Если третий аргумент +, сложить их; 
# если —, то вычесть; * — умножить; / — разделить (первое на 
# второе). В остальных случаях вернуть строку "Неизвестная 
# операция"
def arithmetic(x, y, z):
    if z == '+':
        return x + y
    if z == '-':
        return x - y 
    if z == '*':
        return x * y
    if z == '/':
        return x / y
    else:
        return 'Неизвестная операция'
print(arithmetic(2, 2,'+'))    

# Написать функцию is_prime, принимающую 1 аргумент — число 
# от 0 до 1000, и возвращающую True, если оно четное, и 
# False - иначе.
def is_prime(x):
    if 1 <= x <= 1000:
        if x%2 == 0:
            return True
        else:
            return False
print(is_prime(100))

# Написать функцию is_year_leap, принимающую 1 аргумент — 
# год, и возвращающую True, если год високосный, и False иначе.
def is_year_leap(year):
    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):  
        return 'Given Year is a leap Year'
    else: 
        return 'it is not a leap year'
print(is_year_leap(1980))

import datetime
# Написать функцию date, принимающую 3 аргумента — день, 
# месяц и год. Вернуть True, если такая дата есть в нашем 
# календаре, и False иначе
def date(year, month, day):
    try:
        dt = datetime.datetime(year, month, day)
    except:
        dt = 'none'
    return dt
print(date(2012, 12, 22))

a = [1000, 500, 200, 50]
def bankomat(x):
    result = ''
    a_1000 = 0
    a_500 = 0
    a_200 = 0
    a_50 = 0
    ostatok = x
    if x%a[len(a)-1] == 0:
        if x // a[0] >= 1:
            a_1000 = a_1000 + x // a[0]
            ostatok = x - a[0] * a_1000  
        if ostatok // a[1] >= 1:
            a_500 = a_500 + ostatok // a[1]
            ostatok = ostatok - a[1] * a_500
        if ostatok // a[2] >= 1:
            a_200 = a_200 + ostatok // a[2]
            ostatok = ostatok - a[2] * a_200
        if ostatok // a[3] >= 1:
            a_50 = a_50 + ostatok // a[3]
    else: 
        print('введите номинал, равный 50')
    result = f'{a_1000}-{a[0]},{a_500}-{a[1]},{a_200}-{a[2]},{a_50}-{a[3]}'
    return result
print(bankomat(750))

a = [1000, 500, 200, 50]
def bankomat(x):
    result = ''
    a_1000 = 0
    a_500 = 0
    a_200 = 0
    a_50 = 0
    kupyra_1000 = 1
    ostatok = x
    if x%a[len(a)-1] == 0:
        if x // a[0] >= 1:
            a_1000 = a_1000 + x // a[0]
            if kupyra_1000 >= x // a[0]:
                kupyra_1000 = kupyra_1000 - x // a[0]
                ostatok = x - a[0] * a_1000
            else:
                ostatok = x - a[0] * kupyra_1000
                kupyra_1000 = kupyra_1000 - x // a[0]
        if ostatok // a[1] >= 1:
            a_500 = a_500 + ostatok // a[1]
            ostatok = ostatok - a[1] * a_500
        if ostatok // a[2] >= 1:
            a_200 = a_200 + ostatok // a[2]
            ostatok = ostatok - a[2] * a_200
        if ostatok // a[3] >= 1:
            a_50 = a_50 + ostatok // a[3]
    else: 
        print('введите номинал, равный 50')
    result = f'{a_1000}-{a[0]},{a_500}-{a[1]},{a_200}-{a[2]},{a_50}-{a[3]}'
    return result 
print(bankomat(3750))

def kasseta():
    kupyra_1000 = 5
    kupyra_500 = 5
    kupyra_200 = 5
    kupyra_50 = 5

for x in range(0, 20):
    print('Привіт %s' %x)
    if x < 9:
        break

for x in range(1, 52):
    if x%2 == 0:
        print(x)

y = ['a', 'b', 'c', 'd', 'e']
counter = -1
for x in range(1, 6):
    counter = counter + 1
    print(x,'.', y[counter])
  
weighe = 14
for x in range(1, 16):
    weighe = weighe + 1
    weighe_luna = weighe * 0.165
    print(x, weighe_luna) 
 ''' 
y = ['a', 'b', 'c', 'd', 'e']
for index, x in enumerate(y):
    index = index + 1
    print(index,'.', x)
    
    
    