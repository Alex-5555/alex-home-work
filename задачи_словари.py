# a = [x for x in range(1,13) if x%2 == 0] 
# print(a)
'''
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
'''
from collections import Counter
from functools import reduce
dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}
'''
def sum_dct(*dicts):
    return dict(reduce(lambda x, y: Counter(x) + Counter(y), dicts))
print(sum_dct(dict_1, dict_2))
'''
def max_dct(*dicts):
    return dict(reduce(lambda x, y: Counter(x) | Counter(y), dicts))
print(max_dct(dict_1, dict_2))
