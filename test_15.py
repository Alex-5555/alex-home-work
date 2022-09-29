'''
name? 1
age? 2
[{"name": "1", "age": "2"}]
name? 3
age? 4
[{"name": "1", "age": "2"},{"name":"3", "age": "4"}]


    {"name": "Alex", "ages": "51"},
    {"name": "Dima", "ages": "46"},
    {"name": "Olena", "ages": "49"} 
'''

users = []
while True:
    f = input('как тебя зовут ?  -  ')
    g = input('сколько тебе лет ?  -  ')
    user = {}
    user["name"] = f
    users.append(user)
    print(users)
     