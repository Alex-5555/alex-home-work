'''

Alex - 51
Dima - 47
Aloyna - 49
'''
from email.policy import default
from unicodedata import name


users = [
    {"name": "Alex", "age": 51, },
    {"name": "Dima", "age": 47},
    {"name": "Alyona", "age": 49}]
for user in users:
    # print(x.get("name") + " - " + str(x.get("age")))
    print(f'{user["name"]} - {user["age"]}')