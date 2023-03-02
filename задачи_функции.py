'''
# Напишите функцию sum_range(start, end), которая суммирует все 
# целые числа от значения «start» до величины «end» включительно. 
# Если пользователь задаст первое число большее чем второе, 
# просто поменяйте их местами.
def sum_range(start, end):
    if start > end:
        start, end = end, start
        print(start, end)
    return sum(range(start, end + 1))
print(sum_range(10, 1)) 

# Чтобы проверить понимание параметров и область их видимости, 
# Николай создал 3 функции (представлены ниже). 
# Попытайтесь предугадать, как поведет себя каждая из них при
# запуске (возникнут ли ошибки, что возвратится).
 
def func1():
    param = 4
 
    def inner():
        param += 1
 
    return param
 
 
def func2():
    param = 4
 
    def inner(var):
        var += 1
 
    inner(param)
    return param
 
 
def func3():
    param = 4
 
    def inner(var):
        var += 1
        return var

def func3(a):
    # param = 4
 
    def inner(var):
        var += 1
        return var
    return inner(a)
print(func3(1))

# 1) Первая функция
# Во внутренней функции мы пытаемся воспользоваться внешней 
# переменной. Но она не доступна. Ошибки не возникло по единственной 
# причине: мы эту функцию не вызвали.
# 2) Вторая функция
# Внутренняя функция увеличила значение переменной на 1, но сама она 
# ничего не возвращает (кроме None), поэтому значение param не 
# поменялось.
# 3) Третья функция
# В данном случае вернулось 5, так как мы во внутренней функции 
# увеличили внешнюю переменную и присвоили результат в func3.

# Создайте функцию three_args(), которая принимает 1, 2 или 3 
# строго ключевых параметра. 
# В результате ее работы на печать в консоль выводятся значения 
# переданных переменных, но только если они не равны None. 
# Получим, например, следующее сообщение: «Переданы аргументы: 
# var1 = 2, var3 = 10».
def three_args(*, var1 = 2, var2 = 5, var3 = 10):
    if var1 == None:
        print(f'Переданы аргументы: var2 = {var2}, var3 = {var3}')
    if var2 == None:
        print(f'Переданы аргументы: var1 = {var1}, var3 = {var3}')
    if var3 == None:
        print(f'Переданы аргументы: var1 = {var1}, var2 = {var2}')    
    return var1, var2, var3
print(three_args(var1 = 3, var2 = None, var3 = 11))

def three_args(*, var1, var2 = None, var3 = None):
    arguments = ', '.join([f'{arg[0]} = {str(arg[1])}' for arg in \
                locals().items() if arg[1] is not None])
    print(locals().items())
    return (f'Переданы аргументы: {arguments}') 
print(three_args(var1 = 1, var2 = 'Python'))

def alex(*ttt):
    r = 56
    for y in ttt:
        r = r + y
        print(f'Hello {r}')
    return ('Hello '+ str(r))
print(alex(1,2,3,567))

def three_args(*, var1, var2 = None, var3 = None):
    arguments = ', '.join([f'{arg[0]}={arg[1]}' for arg in \
                locals().items() if arg[1] is not None])
    return (f'Переданы аргументы: {arguments}') 
print(three_args(var1 = 1, var2 = 'Python', var3 = None))

# Антон попал в коллизию: его функция time_now() работает очень 
# странно. Казалось бы, задача простая: показать текущее время с 
# сообщением. Тем не менее, время не меняется. Код предоставлен 
# ниже с примерами. Постарайтесь решить проблему незадачливого 
# программиста.
import datetime
from datetime import timedelta
def time_now():
    time = datetime.datetime.now()
    time_1 = time + timedelta(seconds=1)
    time_n = datetime.time(20, 10, 10)
    return  'Сейчас такое время:' + str(time) + \
            '\nПрошла секунда:' + str(time_1 ) + \
            '\njkljkl:' + str(time_n)    
print(time_now())

# Чтобы лучше разобраться в типах параметров функций Инна создала 
# inspect_function(), которая в качестве аргумента принимает другую 
# функцию (главное, не встроенную, built-in). 
# В результате работы она выводит следующие данные: название 
# анализируемой функции, наименование всех принимаемых ею параметров
# и их типы (позиционные, ключевые и т.п.). 
# Попробуйте повторить результат девушки.
import inspect
# import math
def my_func(a, b, /, c, d, *args, e, f, **kwargs):
	pass

def inspect_function(some_funk):
    print(f'Анализируем функцию {some_funk}')
    for param in inspect.signature(some_funk).parameters.values():
        print (param.name, param.kind, sep=': ')
print(inspect_function(my_func))
'''
from datetime import datetime
def delta_day(d1, d2):
    start_date = datetime.strptime(d1, "%d/%m/%Y")
    print(start_date)
    end_date = datetime.strptime(d2, "%d/%m/%Y")
    print(end_date)
    return (end_date-start_date).days
print(delta_day('10/02/2023', '28/02/2023'))





