import random

name = ['Alex', 'Grischa', 'Sergey', 'Nina', 'Ivan', 'Dima']
faces = ['clubs', 'heart', 'diamond', 'spade']
ranks = ['6','7','8','9','10','A']
koloda = []
for face in faces:
    for rank in ranks:
        koloda.append(f'{face}-{rank}')
random.shuffle(koloda)

'''
getCards('name')->string



'''


players = []
for k in name:
    card = [koloda.pop(), koloda.pop(), koloda.pop()]
    players.append({'name': k, 'cards': card})
print(players)    



