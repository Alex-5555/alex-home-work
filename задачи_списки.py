'''
# Дан произвольный список. Представьте его в обратном порядке.
my_list = [2, 4, 8]
my_list.reverse()
print(my_list)

my_list = [2, 4, 8]
print(my_list[::-1]) 


# Функция to_list() принимает неограниченное количество параметров. 
# Обработайте их так, чтобы на выходе получить список из этих элементов.
def to_list(*args):
    return list(args)
print(to_list(1, 2, 3, 4, 5))

# Николай задумался о поиске «бесполезного» числа на основании списка. 
# Суть оного в следующем: он берет произвольный список чисел, находит самое большое из них, а затем делит его на длину списка. 
# Студент пока не придумал, где может пригодиться подобное значение, но ищет у вас помощи в реализации такой функции useless(s).
def useless(*arks):
    s = list(arks)
    return max(s) / len(s)
print(useless(23, 45, 12, 96, 34))



# Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент. 
# В исходном списке минимум 2 элемента.
def change(lst):
    x = lst.pop(0)
    y = lst.pop(-1)
    lst.append(x)
    lst.insert(0, y)
    return lst
print(change([2, 4, 8]))

def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
print(change([2, 4, 8]))
 
# Требуется создать функцию list_sort(lst), которая сортирует список чисел по убыванию их абсолютного значения.
def list_sort(lst):
    list_ = []
    for a in lst:
        list_.append(abs(a))
    list_.reverse()
    return list_
print(list_sort([2, 8, 5, 56, -12]))

def list_sort(lst):
    lst.sort(key=lambda x: abs(x), reverse = True)
    return lst
print(list_sort([2, 8, 5, 56, -12]))
  
# На входе имеем список строк разной длины. 
# Необходимо написать функцию all_eq(lst), которая вернет новый список из строк одинаковой длины. 
# Длину итоговой строки определяем исходя из самой большой из них. 
# Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов.
# Расположение элементов начального списка не менять.

def all_eq(lst):
    max_item = max(lst, key= lambda x: len(x))
    len_item = len(max_item)
    return [list_.ljust(len_item, '_') for list_ in lst] 
print(all_eq(['крот', 'белка', 'выхухоль']))

def all_eq(lst):
    max_items = {len(a): a for a in lst}
    print(max_items)
    max_ = dict(sorted(max_items.items(), key= lambda x: x[0], \
           reverse = True))
    print(max_)
    list_ = []
    for x, y in max_.items():
        list_.append(y) 
    list_1 = []
    for i in list_:
        if len(i)<len(list_[0]):
            for n in range(0, len(list_[0])-len(i)):
                i = i+'_'
            list_1.append(i)
        else:
            list_1.append(i)
    return list_1
print(all_eq(['крот', 'выхухоль', 'белка']))

def sorts(lst_num):
    lst_num.sort(reverse = True)
    return lst_num
print(sorts([6,5,9,1]))
'''
# отсортировать список [6,4,9,3] по возрастанию (пузырьковый метод);
def sort(lst_num):
    if lst_num[0] < lst_num[1]:
        lst_num
    else:
        lst_num[0], lst_num[1] = lst_num[1], lst_num[0]
    if lst_num[1] < lst_num[2]:
        lst_num
    else:
        lst_num[1], lst_num[2] = lst_num[2], lst_num[1]
    if lst_num[0] < lst_num[1]:
        lst_num
    else:
        lst_num[0], lst_num[1] = lst_num[1], lst_num[0]
    if lst_num[2] < lst_num[3]:
        lst_num
    else:
        lst_num[2], lst_num[3] = lst_num[3], lst_num[2]
    if lst_num[1] < lst_num[2]:
        lst_num
    else:
        lst_num[1], lst_num[2] = lst_num[2], lst_num[1]
    if lst_num[0] < lst_num[1]:
        lst_num
    else:
        lst_num[0], lst_num[1] = lst_num[1], lst_num[0]
    return lst_num
print(sort([1,5,-2,1]))

def sort(lst_num):
    a = True
    for x, y in enumerate(lst_num):
        print(x, y, end='   ')
        try:
            if y > lst_num[x+1]:
                lst_num[x] = lst_num[x+1]
                lst_num[x+1] = y
                a = False
        except:
            pass
    if a == False:
        sort(lst_num)
    return lst_num
print(sort([10,5,-2,1, 11])) 
        








 