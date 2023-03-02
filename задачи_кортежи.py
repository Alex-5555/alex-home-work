'''
# Напишите функцию tpl_sort(), которая сортирует кортеж, состоящий 
# из целых чисел по возрастанию и возвращает его. Если хотя бы один 
# элемент не является целым числом, то функция возвращает исходный 
# кортеж. 
def tpl_sort(tuple_):
    for x in tuple_:
        if not isinstance(x, int):
            return tuple_ 
    return tuple(sorted(tuple_))
print(tpl_sort((1, 4, 23, -5, 29)))

# Функция slicer() на вход принимает кортеж и случайный элемент. 
# Требуется вернуть новый кортеж, начинающийся с первого появления 
# элемента в нем и заканчивающийся вторым его появлением включительно.
# Если элемента нет вовсе – вернуть пустой кортеж.
# Если элемент встречается только один раз, то вернуть кортеж, который
#  начинается с него и идет до конца исходного.
def slicer(tiple_, x):
    if x in tiple_:
        if tiple_.count(x) > 1:
            first_tiple_ = tiple_.index(x)
            end_tiple_ = tiple_.index(x + 1)
            return tiple_[first_tiple_: end_tiple_]
        else:
            return tiple_[tiple_.index(x):]
    else:
        return ()
print(slicer((1, 3, 5, 7, 9, 1, 2), 8))

# Перед студентом стоит задача: на вход функции sieve() поступает 
# список целых чисел. В результате выполнения этой функции будет 
# получен кортеж уникальных элементов списка в обратном порядке.
def sieve(list_a):
    list_a1 = []
    [list_a1.append(x) for x in list_a.reverse() if x not in list_a1]
    return tuple(list_a1)
print(sieve([12, 14, 'agfa', 15, 12, 17]))

def sieve(list_a):
    list_a.reverse()
    list_a1 = []
    for x in list_a: 
        if x not in list_a1:
            list_a1.append(x)
    return tuple(list_a1)
print(sieve([12, 14, 'agfa', 15, 12, 17]))

# Николай знает, что кортежи являются неизменяемыми, но он с этим не 
# готов соглашаться. Ученик решил создать функцию del_from_tuple(), 
# которая будет удалять первое появление определенного элемента из 
# кортежа по значению и возвращать кортеж без оного. Попробуйте 
# повторить шедевр не признающего авторитеты начинающего программиста.
# К слову, Николай не всегда уверен в наличии элемента в кортеже 
# (в этом случае кортеж вернется функцией в исходном виде).
def del_from_tuple(tuple_, element):
    list_ = []
    if element in tuple_:
        for x in tuple_:
            if x != element:
                list_.append(x)
        return tuple(list_)
    else:
        return tuple_
print(del_from_tuple((1, 2, 3, 4, 5), 'on'))

def del_from_tuple(tuple_, element):
    if element in tuple_:
        tuple_index = tuple_.index(element)
        return tuple_[:tuple_index] + tuple_[tuple_index + 1:]
    return tuple_
print(del_from_tuple((1, 2, 3, 4, 5), 3))
'''
# Создайте кортеж из 7-ми именованных кортежей учащихся ВУЗов. 
# В именованном кортеже будут присутствовать следующие поля: 
# имя студента, возраст, оценка за семестр, город проживания. 
# Функция good_students() будет принимать этот кортеж, вычислять 
# среднюю оценку по всем учащимся и выводить на печать следующее 
# сообщение: “Ученики {список имен студентов через запятую} в этом 
# семестре хорошо учатся!”. В список студентов, которые выводятся по 
# результатам работы функции, попадут лишь те, у которых оценка за 
# семестр равна или выше средней по всем учащимся.
from collections import namedtuple
Student = namedtuple('Student3333', 'name age mark city')
students = (
   Student('Елена', '13', 7.1, 'Москва'),
   Student('Ольга', '11', 7.9, 'Иваново'),
   Student('Елизавета', '14', 9.1, 'Тверь'),
   Student('Дмитрий', '12', 5.2, 'Челябинск'),
   Student('Максим', '15', 6.1, 'Самара'),
   Student('Николай', '11', 8.7, 'Владивосток'),
   Student('Артур', '13', 5.8, 'Екатеринбург')
)
def good_students(students):
    total_mark_ = 0
    for student in students:
        total_mark_ +=  student.mark
    mark_ = total_mark_ / len(students)
    good_students_mark = [student.name for student in students if \
                          student.mark >= mark_]
    return 'Ученики ', ', '.join(good_students_mark), 'в этом cеместре хорошо учатся!'
print(good_students(students))
