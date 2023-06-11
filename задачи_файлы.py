'''
# Напишите функцию read_last(lines, file), которая будет открывать
# определенный файл file и выводить на печать построчно последние 
# строки в количестве lines (на всякий случай проверим, что задано 
# положительное целое число). 
# Протестируем функцию на файле «article.txt» со следующим 
# содержимым:

Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела
def read_last(lines, file):
    if type(lines) == int and  lines > 0:
        with open(file, encoding='utf-8') as text:
            file_line = text.readlines()[-lines:]
        for line in file_line:
            print(line.strip())
    else:
        print('Количество строк может быть ' 
                  'только целым положительным числом')
read_last(3, 'article.txt')
read_last(-1, 'article.txt')

# Выберите любую папку на своем компьютере, имеющую вложенные 
# директории. 
# Выведите на печать в терминал ее содержимое, как и всех 
# подкаталогов при помощи функции print_docs(directory).
import os
def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 90)
print(print_docs ('/home/webmaster/zemlyak'))

# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела 
# Требуется реализовать функцию longest_words(file), которая 
# выводит слово, имеющее максимальную длину (или список слов, 
# если таковых несколько).

def longest_words(file):
    with open(file, encoding='utf-8') as text: 
        files = text.read().split()
        word = [x for x in files if len(x) == len(max(files, key=len))]
        return word
print(longest_words('article.txt'))
'''
# Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
# – № - номер по порядку (от 1 до 300);
# – Секунда – текущая секунда на вашем ПК;
# – Микросекунда – текущая миллисекунда на часах.
# На каждой итерации цикла искусственно приостанавливайте скрипт 
# на 0,01 секунды.
import csv
import datetime
import time
with open('rows_00.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, \
        datetime.datetime.now().microsecond])
        time.sleep(0.01)
    