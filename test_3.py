from posixpath import split
import random

faces = ['clubs', 'heart', 'diamond', 'spade']
ranks = ['6','7','8','9','10','J','Q','K','A']
# out = ['6-club','7-club','8-club'....]
deck = []
# выводим масти из списка faces 
for face in faces:
    # print(a)
# присваиваем данным из списка rank масти из списка faces
    for rank in ranks:
        out = str(rank + '-' + face)
        deck.append(out)
        #myout = split(out)
        #print(myout)
random.shuffle(deck)
print(deck)