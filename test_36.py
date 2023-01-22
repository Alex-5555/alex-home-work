import random
import pprint

name = ['Alex', 'Grischa', 'Sergey', 'Nina', 'Ivan', 'Dima']
faces = ['clubs', 'heart', 'diamond', 'spade']
ranks = ['6','7','8','9','10','A']
koloda = []
for face in faces:
    for rank in ranks:
        if rank=='6':
            n = 6
        if rank=='7':
            n = 7
        if rank=='8':
            n = 8
        if rank=='9':
            n = 9
        if rank=='10':
            n = 10
        if rank=='A':
            n = 11
        koloda.append({'faces': face, 'ranks': rank, \
                       'weight': n})
random.shuffle(koloda)
# print(koloda)

players = []
res = []
for k in name:
    card = [koloda.pop(), koloda.pop(), koloda.pop()]
    g = 0
    for j in card:
        g = g + int(j["weight"])
    players.append({'name': k, 'cards': card, 'weight_': g})  
# print(players)
for m in players:
    # print('Уважаемый ' + m['name'], 'получил ' + str(m['weight_']))
    # print(f"Уважаемый {m['name']} получил {m['weit']}")
    # aaa = 'Уважаемый ' + m['name'] + ' получил ' + str(m['weit'])
    aaa = 'Уважаемый %s получил %s first card is - %s-%s' \
           % (m['name'], m['weight_'], m['cards'][0]['faces'], \
           m['cards'][0]['ranks'])
    # aaa = "Уважаемый {0} {1} {0}".format('сам придурок', 'Alex')
    print(aaa)

hhh = "Дарагой {0} {1} {1} {1} Ильич".format('Alex', 'Dima')
print(hhh)
test_36.py