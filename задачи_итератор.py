'''
# Антонина в целях экономии памяти компьютера вместо 
# последовательности чисел от 1 до миллиона в виде списка решила 
# создать ленивый итератор numbers с помощью функции range(). 
# Затем в двух разных местах своего скрипта она делала проверку 
# того, есть ли число 2000 в этой коллекции. 
# В первом случае код вернул True, а во втором False.
# Объясните ученице ее ошибку и предложите способ исправления 
# ситуации.
# numbers = []
for numbers in range(1, 101):
    if numbers == 20:
        print('True' + ',')
    print(numbers, end=',')

# Создайте функцию infinite(lst, tries), которая будет проходиться 
# по элементам списка lst (целые числа) заданное количество раз (tries) циклически. 
# Один раз - один элемент списка. 
# После вывода последнего значения последовательности процедура 
# начнется с самого начала.
# Например, если в списке 2 элемента, а функция получила значение 
# 3, то сначала выведется первый объект, потом последний, а потом 
# опять первый. 
# Результат работы функции представьте в виде строки, состоящей 
# из tries количества символов.
from itertools import cycle
def infinite(lst, tries):
    result = ''
    lst1 = cycle(lst)
    if lst:
        for simbol in range(tries):
            result  += str(next(lst1))
    return result   
print(infinite([1, 2, 3], 4))

# Инструкция yield позволяет создавать генераторы. 
# В отличие от объявления return в функции, где возвращается один 
# объект, yield при каждом вызове функции генерирует новый объект. 
# Фактически это дает возможность использовать генераторы в циклах. 
# Самая важная причина применения такой инструкции - экономия 
# памяти, когда не требуется сохранять всю последовательность, а 
# можно получать ее элементы по одному. 
# Ученик написал генератор show_letters(some_str), выводящий все 
# символы строки на печать, но только в том случае, если они 
# являются буквами (остальные игнорируются). 
# Сократите код функции.
# def show_letters(some_str):
#     clean_str = ''.join([letter for letter in some_str if letter.isalpha()])
#     for symbol in clean_str:
#         yield symbol
# print(show_letters('A!sdf 09 _ w'))

def show_letters(some_str):
    yield from ''.join([letter for letter in
    some_str if letter.isalpha()])
random_str = show_letters('A!sdf 09 _ w')
print(next(random_str))    
print(next(random_str))   
print(next(random_str))   

# Числа Фибоначчи представляют последовательность, получаемую в 
# результате сложения двух предыдущих элементов. 
# Начинается коллекция с чисел 1 и 1. 
# Она достаточно быстро растет, поэтому вычисление больших значений 
# занимает немало времени. 
# Создайте функцию fib(n), генерирующую n чисел Фибоначчи с 
# минимальными затратами ресурсов.
# Для реализации этой функции потребуется обратиться к инструкции 
# yield. 
# Она не сохраняет в оперативной памяти огромную 
# последовательность, а дает возможность “доставать” промежуточные
# результаты по одному. 
def fib(n):
    res = [0, 1]
    for x in range(1, n - 1):
        y = res[-2] + res[-1]
        res.append(y)
    return res
print(fib(7))

def fib(n):
    res = [0, 1]
    for x in range(1, n - 1):
        y = res[-2] + res[-1]
        res.append(y)
        yield res
res_1 = fib(7)
print(next(res_1))
print(next(res_1))
print(next(res_1))

def fib(n):
    fib0 = 0
    # yield fib0
    fib1 = 1
    # yield fib1
    for x in range(n - 2):
        fib0, fib1 = fib1, fib1 + fib0
        print(fib0)
        print(fib1)
        print('s')
        yield fib1
for num in fib(7):
    pass
print(num)

# Реализуйте итератор колоды карт (52 штуки) CardDeck. Каждая 
# карта представлена в виде строки типа «2 Пик». При вызове функции 
# next() будет представлена следующая карта. По окончании перебора 
# всех элементов возникнет ошибка StopIteration.

def carddeck():
    out = []
    faces = ['Пик', 'Черви', 'Бубна', 'Крести']
    ranks = [*range(2, 11),'J','Q','K','A']
    for x in ranks:
        for y in faces:
            out.append(str(x) + ' ' + y)    
    return out

card_only = carddeck()
card_only.reverse()

while card_only:
    x = card_only.pop()
    print(x)
'''
class CardDesk:
    def __init__(self):
        self.min = 0
        self.max = 52
        self.__RANKS = [*range(2, 11),'J','Q','K','A']
        self.__FACES = ['Пик', 'Черви', 'Бубна', 'Крести']

    def __len__(self):
        return self.max

    def __next__(self):
        if self.min >= self.max:
            raise StopIteration
        else:
            ranks = self.__RANKS[self.min % len(self.__RANKS)]
            faces = self.__FACES[self.min // len(self.__RANKS)]
            self.min += 1
            return f'{ranks} {faces}'

    def __iter__(self):
        return self

desk = CardDesk()
# print(desk)
while True:
    print(next(desk))
