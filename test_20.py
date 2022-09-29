'''
# завдання 1: створити список цілих чисел від 1 до 12 за допомогою циклу:
# відповідь:
# а) створюємо умовну змінну numbers_month та присвоюємо їй значення порожнього 
   списку: 
numbers_month = []
# б) за допомогою оператора циклу for та вбудованої функщії range генеруємо у 
# змінну а список з 12 цілих чисел від 1 до 12:
for a in range(1, 13):
# в) за допомогою методу append додаємо у порожній список змінної numbers_month
#    згенеровані у змінну а 12 цілих чисел від 1 до 12:
    numbers_month.append(a)
# г) роздоуковуємо змінну numbers_month:
print(numbers_month)

або:
створюємо список цілих чисел від 1 до 12 за допомогою генервтора списку
і функції range:
numbers_month = [x for x in range(1, 13)]
print(numbers_month)

або:
формуємо список цілих чисел за допомогою функції list та генератора range:
list(range(1,13))


numbers = list(range(1,13))
numbers_odd = []
for x in numbers:
    if x%2 == 0:
        numbers_odd.append(x) 
print(numbers_odd)

або:

а = [x for x in range(1,13) if x%2 == 0]

подвоюємо значення цілих чисел у списку:
numbers_month = [x*2 for x in range(1, 13)]
print(numbers_month)

# завдання 2: створити словник, в якому кожному цілому числу зі списку 
# numbers_month буде відповідати назва місяця:
# а) формуємо список із назвою місяців:
months = [january, February, March, April, May, June, 
         July, August, September, October, november, December]
# б) із використанням генервтора цілих чисел range та оператора zip 
# створюємо словник numbers_month:
numbers_month = {x : y x,y in zip(numbers_month, months)}
'''
'''

a = input('Введи любое число от 1 до 12 - ')
if int(a) == 12 or int(a) == 1 or int(a) == 2: 
    print('winter')
if int(a) == 3 or int(a) == 4 or int(a) == 5: 
    print('Spring')
if int(a) == 6 or int(a) == 7 or int(a) == 8: 
    print('summer')
if int(a) == 9 or int(a) == 10 or int(a) == 11: 
    print('autumn')
'''

# завдання 1: створити функцию season,  яка приймає в якості аргумента
# номер місяця, та повертає рядок із назвою сезону року: 
# відповідь:
# а) створюємо за допомогою ключового слова def функцию season, яка  
#    приймає в якості аргумента змінну а: 
def season(a):
# б) використовуючи умовний оператор if та логічний оператор or створюємо 
# набір умов для визначення номерів зимових місяців, повертаємо рядок winter:    
    if a == 12 or a == 1 or a == 2: 
        return ('winter')
# в) здійснюємо аналогічні дії щодо інших значень аргумента а:
    if a == 3 or a == 4 or a == 5: 
        return('Spring')
    if a == 6 or a == 7 or a == 8: 
        return('summer')
    if a == 9 or a == 10 or a == 11: 
        return('autumn')
# г) за допомогою оператора input виводимо у консоль рядок у дужках, 
# запрошуємо у користувача ввести номер місяця, зберігаючи його у зиінній а: 
a = int(input('Введи любое число от 1 до 12 - '))
# д) викликаємо функцию season зі змінною а:
print(season(a))

