from os import remove
from posixpath import split


t = '4,6,8'
# b = list(map(int, t.split(','))) 
b = [int(x) for x in t.split(',')]
c = sum(b)
print(c)

