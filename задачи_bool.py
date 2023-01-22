'''
# Напишите функцию dislike_6(a), которая всегда возвращает True, если только не передается число 6 типа int или типа float (в данном случае она вернет «Только не 6!»)
def dislike_6(a):
    if a == float(6) and int(6):
        return "Только не 6"
    return True
print(dislike_6(6.0))

def dislike_6(a):
    if (type(a) is float or type(a) is int) and a == 6.0:
        return "Только не 6"
    return True
print(dislike_6(5.0))

# Изучающий язык Python студент постоянно путается в свойствах логических операций (ассоциативность, дистрибутивность, коммутативность, правило де Моргана). 
# Он решил написать функцию-подсказку help_bool(letter), которая принимает одну из 4 букв: к, а, д, м (соответствующую каждому свойству). 
# Результат выполнения: определенное правило работы в виде строки.
# Если будет передано что-то иное, то вернется подсказка-строка с пояснением по каждому возможному аргументу.
def help_bool(letter):
    if letter == 'a':
        return 'A or (B or C) == (A or B) or C == A or B or C \
                A and (B and C) == (A and B) and C == A and B and C'
    if letter == 'k':
        return 'A or B = B or A \
                A and B = B and A'
    if letter == 'd':
        return 'A and (B or C) == (A and B) or (A and C) \
                A or (B and C) == (A or B) and (A or C)'
    if letter == 'm':
        return 'not (A or B) == not A and not B \
                not (A and B) == not A or not B \
                not (A < B) == A >= B \
                not (not (A)) = A'
    return 'Возможные аргументы: k – Коммутативность, \
                                 d – Дистрибутивность, \
                                 а – Ассоциативность, \
                                 m – Теорема Де Моргана'
print(help_bool('c'))

# Дано 2 скрипта. В первом – возникает ошибка, во втором – ошибки нет. 
# Поясните почему.

# Скрипт 1.
a = None
if len(a) > 0 and a is not None:
    print('OK') 

# Скрипт 2.
a = None
if a is not None and len(a) > 0:
    print('OK')   
# Применение оператора and к выражениям останавливается тогда, когда обнаруживается первое ложное значение. None – ложное значение, поэтому оно сразу возвращается, без вычисления второй половины выражения во втором скрипте.
# В первом же примере мы пытаемся найти длину None, а такого свойства у значения нет. Поэтому возникает ошибка.
'''                        
def divider(a, b):
    return b and (a / b) ** 3 or 'Нули в знаменателе не приветствуются'
print(divider(10, 0))