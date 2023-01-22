from heapq import nlargest

'''
# 
b = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for j in a:
    if j<5:
        b.append(j)
print(b)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for j in a:
    if j <5:
        print(j)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([j for j in a if j<5])

# 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print([j for j in b if j in a])

c = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for j in b:
    if j in a:
        c.append(j)
print(c)


c = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = list(set(a) & set(b))
print(c)

#  
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_values = sorted(d.values())
# print(sorted_values)
sorted_d = {}
for j in sorted_values:
    for h in d.keys():
        if h == j:
            sorted_d[h] = d[h]
print(sorted_d)

# 
dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}
result = {}
for j in(dict_a, dict_b, dict_c):
    result.update(j)
print(result)

result = {**dict_a, **dict_b, **dict_c}
print(result)

# 
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
val = [] 
for j in my_dict.values():
    val.append(j)
print(val)
val.sort()
print(val)
b = []
counter = 0
while counter<3:
    counter = counter +1
    a = val.pop()
    b.append(a)
print(b)

# 
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
result = nlargest(3, my_dict, key=my_dict.get)

# 
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
val = []
for j in my_dict.items():
    val.append(j)
print(val[0][1])
for h in val:
    print(h)

# 
a = [19, 11, 14, 5, 7, 35, 23]
b = a.index(5, 1, 5)
print(b)

# 
list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
list.append('Alex')
print(list)
list.insert(5, 7)
print(list)
list_2 = [1, 3, 5]
list.append(list_2)
print(list)
a = (7, 9, 11)
list.insert(3, a)
print(list)
print(list[0])
list.remove(7)
print(list)
c = list.count(1)
print(c)
'''
# 
list = ['Нулевой элемент', 'One', 2, 3, 4, (5, 5, 5)]
a = list[0][-1]
print(a)

b = 100
c = 'Строка'
print(b, c)
f = b
b = c
c = f
# print(b, c)



list = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7]
h = set(list)
print(h)
len(list) == len(h)
print()


