# d = [4,8,340,76,24,86,42]
# d.sort()
# # print(d)
# a = d.pop()
# print(a)
# max = 0
# for a in d:
#     if a > max:
#         max = a
# print(max)

'''
h = ['dima', 'alex', 'den', 'fedotka', 'jjjjjjjjjjjjjjjjj']
max = 0
for a in h:
    b = len(a)
    if b > max:
        max = b
print(max)


# print(maxlen(h))
h = ['dima', 'alex', 'den', 'fedotka', 'jjjjjjjjjjjjjjjjj']
def maxlen(h):
    max = 0
    for a in h:
        b = len(a)
        if b > max:
            max = b
    return max
#print(maxlen(h)) 

'''
from test_3 import deck, deck_s, dial
a = deck()
b = deck_s(a)
c = dial(b,2)
print(c)
# print(dial(deck_s(deck())))

