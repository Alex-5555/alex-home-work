from traceback import format_exception
from unicodedata import name

a = [{'name': 'Nadya', 'child': [
                                 {'name': 'Dima'}, 
                                 {'name': 'Vera'}]
    }, 
    {'name': 'Dima', }]
for b in a:
    print(b['name'])

a[0]['child'] = [{'name': 'Dima'}, {'name': 'Vera'}]
a[1]['child'] = [{'name': 'Bogdan'}]
print(a)
for s in a:
    for i in s['child']:
        print(i['name'])
    # print(s['child'][0]["name"])




'''