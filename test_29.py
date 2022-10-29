g = [
    {"face": "q", "value": 4 },
    {"face": "a", "value": 5 },
    {"face": "d", "value": 6 },
    {"face": "q", "value": 7 },
    {"face": "q", "value": 8 }
]
ff = []
for i in g:
    ff.append(i['face'])
print(ff)
r = {}
for i in set(ff):
    r[i] = 0
print(r)
'''
for i in g:
    r[i["face"]] = r[i["face"]]+i["value"]
print(r)
'''