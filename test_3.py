'''
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
'''


import random

def deck():
    faces = ['clubs', 'heart', 'diamond', 'spade']
    ranks = ['6','7','8','9','10','J','Q','K','A']
    out = []   
    for face in faces:
        for rank in ranks: 
            out.append(face+rank) 
    return out
    
def deck_s(deck):
    random.shuffle(deck)
    return deck 

def dial(deck,counter=5):
    b = []
    # a = deck.pop()   
    # b = deck.pop()
    # c = deck.pop()
    # d = deck.pop()
    # e = deck.pop()
    for x in range(0, counter): 
        b.append(deck.pop())

    return b

 
        # print(out)   
#         out = str(face+'-'+rank)
#         my_out = out.append()
# print(my_out)


#     
# print(deck(my_out))