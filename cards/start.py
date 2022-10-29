from lib import Koloda
koloda = Koloda()
#karty = koloda.daymne()
#print(karty)
users = ['Dima', 'Alex']
points = [0,0]
for index, user in enumerate(users):
    print(f'{user} got this fucking cards')
    cards = koloda.dial()
    points[index] = koloda.sum(cards)
    

print(points)
print(max(points))
print(users[points.index(max(points))])