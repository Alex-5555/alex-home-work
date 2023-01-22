import random

name = ['Alex', 'Grischa', 'Sergey', 'Nina', 'Ivan', 'Dima']

faces = ['clubs', 'heart', 'diamond', 'spade']
ranks = ['6','7','8','9','10','A']
koloda = []
for face in faces:
    for rank in ranks:
        koloda.append(f'{face}-{rank}')
random.shuffle(koloda)
# print(koloda) g = [j.pop(), j.pop()]; h.append([j.pop(), j.pop()])

c_1 = []
counter = 0
while counter<3:
    counter = counter + 1
    b_1 = koloda.pop()
    c_1.append(b_1)
# print(c_1)

c_2 = []
counter = 0
while counter<3:
    counter = counter + 1
    b_2 = koloda.pop()
    c_2.append(b_2)
# print(c_2)

c_3 = []
counter = 0
while counter<3:
    counter = counter + 1
    b_3 = koloda.pop()
    c_3.append(b_3)
# print(c_3)

c_4 = []
counter = 0
while counter<3:
    counter = counter + 1
    b_4 = koloda.pop()
    c_4.append(b_4)
# print(c_4)

c_5 = []
counter = 0
while counter<3:
    counter = counter + 1
    b_5 = koloda.pop()
    c_5.append(b_5)
# print(c_5)

c_6 = []
counter = 0
while counter<3:
    counter = counter + 1
    b_6 = koloda.pop()
    c_6.append(b_6)
# print(c_6)

c_res = [c_1, c_2, c_3, c_4, c_5, c_6] 
# print(c_res)

d = dict.fromkeys(['name', 'cards'])
#d = {"name": None}
h = []
for i in name:
    h.append({"name": i})
print(h)

'''
for f in name:
    d.update({'name': f})
for g in c_res:
    d.update({'name': f, 'cards': g})
    print(d)
'''

