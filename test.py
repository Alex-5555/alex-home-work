#  импорт библиотеки случайностей
import random

# генерируем 36 чисел, перемешиваем,"срезаем" первые 5 и помещаем в список 
ggg = list(range(1,36))
random.shuffle(ggg)
num_lot = ggg[0:5]

# запросили ввод пяти чисел
mynum = input('выбери пять произвольных чисел в диапазоне от 1 до 36 через запятую: ')
mynum_list = list(map(int, mynum.split(','))) 
print(mynum_list)
# вывели список
print(ggg[0:5])
# сделаем счетчик угадываний
counter = 0

# пойдем циклом по числам пользователя
for user_number in mynum_list:
# для каждого числа пойдем циклом по выиграшным номерам
    for win_number in num_lot:
        # определяем угадал ли пользователь
        print(f'сравниваем {user_number} с {win_number}')
        if user_number == win_number:
            counter = counter + 1
# выводим результат угадываний на экран
print(f'Вы угадали {counter} раз.')
# присваиваем переменной а значение счетчика угадываний
a = int(counter)
if a == 3: 
    print('Вы выиграли 100,00 грн.!')
elif a == 4:
    print('Вы выиграли 1 000,00 грн.!!')
elif a == 5:
    print('Вы выиграли 10 000,00 грн.!!!')
else:
    print('Вы ничего не выиграли @')


