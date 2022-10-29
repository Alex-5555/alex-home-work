a = {1:2}
print(a)

a = dict.fromkeys([1,2], 100)
print(a)

a = {x: x**2 for x in range(7)}
print(a)

a = dict(hh = 'uuuu', mm="kjkj")
print(a)

# a = dict(**kwargs)

# a = dict([(1, 1), (2, 4)])
# print(a)

d = {1: 2, 2: 4, 3: 9}
print(d[1])
d[4] = 4 ** 2
print(d)

dict.copy(d)
print(d)

# dict.clear(d)
# print(d)

c = dict.keys(d)
print(list(c))

# del d[1]
# print(d)

d.update({5:25, 6:36})
print(d)

c = d.get(8,'nihera')
#c = d[8]
print(c)

a = [1, 2, {'age':5, "users": [2,3,{'name':'Alex'}]}]
b = a[2]['users'][2]['name']
print(b)

a = {1: 2, 2: 4, 3: 9}
for b, v in a.items():
    print(b, v)


numbers_month = [x for x in range(1, 13)]
months = ['january', 'February', 'March', 'April', 'May', 
          'June', 'July', 'August', 'September', 'October',
          'november', 'December']
# print(numbers_month)
# print(months)
numbers_months = {x: y for x, y in zip(numbers_month, months)}
print(numbers_months)
# print(list(zip(numbers_month, months)))
# print(dict(zip(numbers_month, months)))

dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 1:60}
result = {}
for d in (dict_a, dict_b, dict_c):
    result.update(d)
print(result)

