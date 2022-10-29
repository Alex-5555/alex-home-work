from json.tool import main
import random
# import pdb

faces = ['clubs', 'heart', 'diamond', 'spade']
ranks = ['6','7','8','9','10','J','Q','K','A']
koloda = []
for face in faces:
    for rank in ranks:
        if rank == '6':
            g = 6
        if rank == '7':
            g = 7
        if rank == '8':
            g = 8
        if rank == '9':
            g = 9
        if rank == '10':
            g = 10
        if rank == 'J':
            g = 3
        if rank == 'Q':
            g = 4
        if rank == 'K':
            g = 5
        if rank == 'A':
            g = 11
        koloda.append({"value":f'{face}-{rank}', "count": g})
random.shuffle(koloda) 
print(koloda)
'''
a = dict.fromkeys(['clubs-6', 'heart-6', 'diamond-6', 'spade-6'], 6)
b = dict.fromkeys(['clubs-7', 'heart-7', 'diamond-7', 'spade-7'], 7)
c = dict.fromkeys(['clubs-8', 'heart-8', 'diamond-8', 'spade-8'], 8)
d = dict.fromkeys(['clubs-9', 'heart-9', 'diamond-9', 'spade-9'], 9)
e = dict.fromkeys(['clubs-10', 'heart-10', 'diamond-10', 'spade-10'], 10)
f = dict.fromkeys(['clubs-J', 'heart-J', 'diamond-J', 'spade-J'], 3)
g = dict.fromkeys(['clubs-Q', 'heart-Q', 'diamond-Q', 'spade-Q'], 4)
h = dict.fromkeys(['clubs-K', 'heart-K', 'diamond-K', 'spade-K'], 5)
k = dict.fromkeys(['clubs-A', 'heart-A', 'diamond-A', 'spade-A'], 11)
result = {}
for x in (a, b, c, d, e, f, g, h, k):
    result.update(x)
print(result)

for face in faces:
    for rank in ranks:
        koloda.append(f'{face}-{rank}')
random.shuffle(koloda) 
print(koloda)
'''
player_1 = []
res_1 = []
name_1 = input('как тебя зовут ? - ')
# player_1.append(name_1)
max = 'a'
input('чтобы получить карту нажми enter - ')
while max=='a':
    carde_1 = koloda.pop()
    player_1.append(carde_1['value'])
    print(player_1)
    res_1.append(carde_1['count']) 
    print(sum(res_1))
    max = input('еще карту? - нажми a, достаточно? - нажми x - ')
summa_1 = input('подсчитать результат - ')    
summa_1 = sum(res_1)
print(summa_1)

player_2 = []
res_2 = []
name_2 = input('как тебя зовут ? - ')
# player_2.append(name_2)
max = 'a'
input('чтобы получить карту нажми enter - ')
while max=='a':
    carde_2 = koloda.pop()
    player_2.append(carde_2['value']) 
    print(player_2)
    res_2.append(carde_2['count'])
    print(sum(res_2))
    max = input('еще карту? - нажми a, достаточно? - нажми x - ')
summa_2 = input('подсчитать результат - ')    
summa_2 = sum(res_2)
print(summa_2)

if summa_1>summa_2:
    print('выиграл '+name_1)
if summa_1 == summa_2:
    print('ничья')
if summa_1<summa_2:
    print('выиграл '+name_2)

    
