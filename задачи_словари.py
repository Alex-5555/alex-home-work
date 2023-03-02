'''
# a = [x for x in range(1,13) if x%2 == 0] 
# print(a)

date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(
    **date_info,
    **track_info
 ) 
print(filename)   


def to_dict(lst):
    return {element: element for element in lst}
print(to_dict([1, 2, 3, 4, 5]))


d = {'a': 1, 'b': 2, 'c': 3}
print(d.items())


my_dict = {'first_one': 'we can do it'}
def biggest_dict(**kwargs):
    my_dict.update(**kwargs)
biggest_dict(a = 1)
print(my_dict) 

def count_it(sequense):
    num_dict = {int(item): sequense.count(item) for item in sequense}
    sort_num_dict = sorted(num_dict.items(), key=lambda x: x[1])       
    return dict(sort_num_dict[-4:])     
print(count_it('11115657770009'))

dict_Alex = {x: x*2 for x in range(1, 6)}
# print(dict_Alex)
a = dict_Alex.pop(5)
# print(a)
b = dict_Alex.pop(1)
# print(b)
dict_Alex[1] = b
print(dict_Alex)
dict_Alex['new_key'] = 'new_value'
print(dict_Alex)
dict_Alex_1 = {5: a}
print(dict_Alex_1)
for k, j in dict_Alex.items():
    dict_Alex_1[k] = j
print(dict_Alex_1)


dict_Alex = {x: x*2 for x in range(1, 6)}
lst = list(dict_Alex.items())
lst.insert(0, ('new_key', 'new_value'))
dict_Alex_1 = dict(lst)
print(dict_Alex_1)

# from collections import OrderedDict
dict_Alex = {x: x*2 for x in range(1, 6)}
dict_Alex_1 = {'new_key': 'new_value'} | dict_Alex
print(dict_Alex_1)

from collections import Counter
from functools import reduce
dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}

def sum_dct(*dicts):
    return dict(reduce(lambda x, y: Counter(x) + Counter(y), dicts))
print(sum_dct(dict_1, dict_2))

def max_dct(*dicts):
    return dict(reduce(lambda x, y: Counter(x) | Counter(y), dicts))
print(max_dct(dict_1, dict_2))

# Напишите функцию to_dict(lst), которая принимает аргумент 
# в виде списка и возвращает словарь, в котором каждый элемент 
# списка является и ключом и значением. Предполагается, что 
# элементы списка будут соответствовать правилам задания ключей 
# в словарях. 
def to_dict(lst):
    return {x: x for x in lst}
print(to_dict([1, 2, 3]))

# Иван решил создать самый большой словарь в мире. Для этого он 
# придумал функцию biggest_dict(**kwargs), которая принимает 
# неограниченное количество параметров «ключ: значение» и обновляет 
# созданный им словарь my_dict, состоящий всего из одного элемента 
# «first_one» со значением «we can do it». Воссоздайте эту функцию.
my_dict = {'first_one': 'we can do it'}
my_dict = {'first_one': 'we can do it'}
def biggest_dict(**kwargs):
    my_dict.update(**kwargs)
    return my_dict
print(biggest_dict(a = 'b', c = 'd'))

# Дана строка в виде случайной последовательности чисел от 0 до 9. 
# Требуется создать словарь, который в качестве ключей будет 
# принимать данные числа (т. е. ключи будут типом int), а в качестве
# значений – количество этих чисел в имеющейся последовательности. 
# Для построения словаря создайте функцию count_it(sequence), 
# принимающую строку из цифр. Функция должна возвратить словарь 
# из 3-х самых часто встречаемых чисел.
def count_it(sequence):
    dict_ = {int(x): sequence.count(x) for x in sequence}
    tuple_ = sorted(dict_.items(), key = lambda y: y[1], reverse=True)
    dict_res = dict(tuple_[:3])
    return dict_res
print(count_it('13524617835726374764'))

from collections import Counter
def count_it(sequence):
    return dict(Counter([int(x) for x in sequence]).most_common(3))
print(count_it('13524617835726374764'))

# Создайте словарь с количеством элементов не менее 5-ти. 
# Поменяйте местами первый и последний элемент объекта. 
# Удалите второй элемент. Добавьте в конец ключ «new_key» 
# со значением «new_value». Выведите на печать итоговый словарь. 
# Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
dict_ = {1: 2, 'name': 'Alex', 'x': 'y', 5: 7, 'free': 'end'}
print(dict_)
dict_list = list(dict_.items())
x = dict_list.pop()
y = dict_list.pop(0)
dict_ = dict(dict_list)
print(dict(dict_))
dict_.update([y])
print(dict_)
dicts_ = {}
dicts_ ['free'] = 'end'
print(dicts_)
dicts_.update(dict_)
print(dicts_)
dicts_list = list(dicts_.items())
dicts_list.pop(1)
dict_ = dict(dicts_list)
print(dict_)
dict_['new_key'] = 'new_value'
print(dict_)

# Имеется ряд словарей с пересекающимися ключами 
# (значения - положительные числа). Напишите 2 функции, которые 
# делают с массивом словарей следующие операции:
# 1-ая функция max_dct(*dicts) формирует новый словарь по правилу:
# Если в исходных словарях есть повторяющиеся ключи, выбираем среди 
# их значений максимальное и присваиваем этому ключу (например, 
# в словаре_1 есть ключ “а” со значением 5, и в словаре_2 есть ключ 
# “а”, но со значением 9. Выбираем максимальное значение, т. е. 9, 
# и присваиваем ключу “а” в уже новом словаре).  Если ключ не 
# повторяется, то он просто переносится со своим значением в новый 
# словарь (например, ключ “с” встретился только у одного словаря, 
# а у других его нет. Следовательно, переносим в новый словарь этот 
# ключ вместе с его значением). Сформированный словарь возвращаем.
# 2-ая функция sum_dct(*dicts) суммирует значения повторяющихся 
# ключей. Значения остальных ключей остаются исходными. (Проводятся 
# операции по аналогу первой функции, но берутся не максимумы, а 
# суммы значений одноименных ключей). Функция возвращает 
# сформированный словарь.
from collections import Counter
from functools import reduce
# dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
# dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
# dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
# dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}
def max_dct(*dicts):
    return dict(reduce(lambda a, b: Counter(a) | Counter(b), dicts))
print(max_dct({1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90},\
              {1: 12, 3: 7, 4: 1, 5: 2, 7: 112},\
              {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71},\
              {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}))
'''
from collections import Counter
from functools import reduce
def max_dct(*dicts):
    return dict(reduce(lambda a, b: Counter(a) + Counter(b), dicts))
print(max_dct({1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90},\
              {1: 12, 3: 7, 4: 1, 5: 2, 7: 112},\
              {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71},\
              {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}))


