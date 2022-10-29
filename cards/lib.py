'''
def deck():
    faces = ['clubs', 'heart', 'diamond', 'spade']
    ranks = ['6','7','8','9','10','J','Q','K','A']
    out = []   
    for face in faces:
        for rank in ranks: 
            out.append(face+rank) 
    return out

from cards.lib import Koloda
koloda = Koloda()
karty = koloda.daymne()
'''
import random
class Koloda():
    def __init__(self):
        self.cards = self.create_deck()
        self.mix()

    def create_deck(self):
        faces = ['clubs', 'heart', 'diamond', 'spade']
        self.ranks = ['6','7','8','9','10','J','Q','K','A']
        self.points = [6,7,8,9,10,11,12,13,14]
        out = []   
        for face in faces:
            for rank in self.ranks: 
                out.append(face+'_'+rank) 
        return out

    def mix(self):
        random.shuffle(self.cards)
        
    def dial(self):
        dial_6 = [
        self.cards.pop(), 
        self.cards.pop(), 
        self.cards.pop(), 
        self.cards.pop(), 
        self.cards.pop(), 
        self.cards.pop()
        ]
        return dial_6

    def sum(self, cards):
        points = 0
        for card in cards:
            print(card)
            r = card.split('_')[1]
            ind = self.ranks.index(r)
            ''' 
            if r == '9':
                points = points + 9
            if r == '10':
               points = points + 10
            if r == '6':
               points = points + 6
            if r == '7':
               points = points + 7
            if r == '8':
               points = points + 8
            if r == 'J':
               points = points + 4
            if r == 'D':
               points = points + 5
            if r == 'K':
               points = points + 11
            if r == 'A':
               points = points + 12
            '''
            points  = points + self.points[ind]    
        return points

    ''' 
    def sum(self):
        alex_sum = 
        dima_sum = 
        if alex_sum > dima_sum:
            print(/////)
        elif:
            print(??????)
    '''

            
        