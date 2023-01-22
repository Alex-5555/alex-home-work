# завдання 1,2: створити список цілих чисел, що відповідає певній умові: 
# а) створюємо список довільних цілих чисел, поміщюючи його до змінної а:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# за допомогою оператора циклу for та логічного оператора if поміщаємо у,
# змінну х список з цілих чисел, що є меньшими або дорівнюють 5: 
for x in a:
    if x<=5:
#роздруковуємо змінну х:
        print(x)
'''
або:
вза допомогою оператора циклу for та логічного оператора 
 if формуємо генератор списку щ певною умовою:   
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([x for x in a if x<=5])
 
# Завдання 1,3: сформувати список, що складається з однакових 
# аргументів списків а та б: 
# формуємо списки а та б:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# за допомогою оператора циклу for та логічного оператора if
# формуємо список result, який виводимо на екран за допомогою
# оператора print:
result = [x for x in a if x in b]
print(result)

# або:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89]
# result = list(set(a) & set(b))
# print(result)

# Завдання 4: Створити словник. 
# a) створюєио словник:
# a = {}
# або:
a = dict([(1, 2), (2, 4), (3, 9)])
print(a)
# б) зв допомогою метода fromkeys створюєио словник із одним завданим
# значенням для всіх приведених ключів:
a = dict.fromkeys([1, 2, 3], 100)
print(a)

# б) з використанням оператора for та генератора списку цілих чисел range
# створюєио словник із парами ключх [х] та значенням x**2: 
# a = {x:x**2 for x in range(5)}
# print(a)

# Завдання 4: розкласти словник на ключ та значення ('розмапити'): 
# а) за допомогою оператора цикла for та метода items() друкуємо пари 
# ключ-значення за аналогією з кортежами у списку: 
a = {1: 2, 2: 4, 3: 9}
for b, v in a.items():
    print(b, v)

# зі списку а отримуємо значення, шр відповідає ключу 1:   
#  print(a[1]) 
# до списку а додаємо пару ключ-значення 4:16:
# a[4] = 4**2
# # print(a)
# друкуємо  ключі змінної а:
# print(*a)

# def h(*args, **wargs):
#     print(args[0])
#     print(kwargs["name"])
# h(44,6,6, name="Dima")

dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 1:60}
result = {}
for d in (dict_a, dict_b, dict_c):
    result.update(d)
print(result)

# префіксні опеоатори * та **:
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
# print(fruits[0], fruits[1], fruits[2], fruits[3])
print(*fruits)

def add(*args):
    result = 0
    for i in args:
        result = result + i
    return result
b = add(1,2,3,4)
print(b)

# numbers = [2, 1, 3, 4, 7]
# more_numbers = [*numbers, 11, 18]
# print(*more_numbers)

# fruits = ['lemon', 'pear', 'watermelon', 'tomato']
# numbers = [2, 1, 3, 4, 7]
# print(*fruits, *numbers)

# date_info = {'year': "2020", 'month': "01", 'day': "01"}
# track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
# filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(
#     **date_info,
#     **track_info
# ) 
# print(filename)     

# from random import randint
# def roll(*dice):
#     return sum(randint(1, die) for die in dice)
# print(roll(6, 6))