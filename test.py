#!/usr/bin/python3
# name = input('What is your name?')
# print('Hello ' + name)
# age = input('What is your age?')
# print(name +' Jor ' + age)
# /from unicodedata import name


# name = input('как тебя зовут ') 
# print(f'Hello {name}')

# import random

# num = random.randint(1,3)
# print(num)

# stop = True
# while stop:
#     mynum = input('угадай число') 
#     if int(mynum) == num:
#         print('Uraaaaaaaa')
#         stop = False
#     else:
#         print('Noooooooooo')

# num = random.randint(1,9)
# print(num)

# mynum = input('угадай число') 
# if int(mynum) == num:
#     print('Uraaaaaaaa')
# else:
#     print('Noooooooooo')
# импорт библиотеки случайностей
import random

# генерируем 6 чисел
num_1 = random.randint(1,36)
num_2 = random.randint(1,36)
num_3 = random.randint(1,36)
num_4 = random.randint(1,36)
num_5 = random.randint(1,36)

# вставили в спсок случайные числа
num_lot = [num_1, num_2, num_3, num_4, num_5]
# вывели список
print(num_lot)

# запросили ввод пяти чисел
mynum = input('выбери пять произвольных чисел в диапазоне от 1 до 36 через запятую: ')
mynum_list = list(map(int, mynum.split(','))) 
print(mynum_list)

# сделаем счетчик угадываний
counter = 0

#пойдем циклом по числам пользователя
for user_number in mynum_list:
    # для каждого числа пойдем циклом по выиграшным номерам
    for win_number in num_lot:
        # определяем угадал ли пользователь
        print(f'сравниваем {user_number} с {win_number}')
        if user_number == win_number:
            counter = counter + 1

print(f'Вы угадали {counter} раз.')

# if   num_lot == mynum_list:
#     print("Ура, я миллионер!")
# else:
#     print("Вот так всегда!")


