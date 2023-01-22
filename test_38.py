import datetime
from datetime import date
'''
def Alex(f):
    print('Hello_' + str(f))
Alex(2)

def Alex(f):
    print('Hello_%s' %f)
Alex(2)

def Alex(f):
    print(f'Hello_{f}')
Alex(2)

def Alex(f):
    print('Hello_{0}'.format(f))
Alex(2)

def Alex(f, g):
    print('Hello_{0}{1}_{0}'.format(f, g))
Alex(2, 3)

o = [1,2,3,1]
def Alex(o, x = 3):
    if len(set(o)) != x:
        return True
    else:
        return False
print(Alex(o))


def A(er):
    return datetime.date.today().year - er

def B(m):
    t = []
    for j in m:
        t.append(datetime.date.today().year-j)
    return t
print(B([1970, 1975, 1978]))


def A(er):
    return datetime.date.today().year - er

def B(m):
    t = []
    for j in m:
        t.append(A(j))
    return t
print(B([1970, 1975, 1978]))


# def [дата рождения - кол-во прожитых дней] - 3 функции
# d0 = date(2011, 1, 8)
# d1 = date(2015, 8, 16)
# delta = d1 - d0
# print('The number of days between the given range of dates is :')
# print(delta.days)

# def [дата рождения - кол-во прожитых дней] - 3 функции
def Number_of_days(year, month, day):
    delta = date.today() - date(year, month, day)
    return delta 
# print(Number_of_days(1970, 9, 15))
#########################################
def broker():
    return 'I am broker'

def go(func, year, month, day):
    return func(year, month, day)
##########################################

years = [1970, 1977]
for s in years:
    print(go(Number_of_days, s, 9, 15))
##########################################
'''
# 
# def [дата рождения - кол-во прожитых дней] - 3 функции
def Number_of_days(year, month, day):
    delta = date.today() - date(year, month, day)
    return delta 
# print(Number_of_days(1970, 9, 15))
#########################################
def broker():
    return 'I am broker'

def go(func, date, seps):
    for s in seps:     
        g = date.split(s)
        if len(g)==3:
            year = int(g[0])
            month = int(g[1])
            day = int(g[2])
    return func(year, month, day)
             
          
##########################################

years = ['1970_06_09', '1977-05-04']
for s in years:
    print(go(Number_of_days, s, ['/','-', '_']))
##########################################

# 




