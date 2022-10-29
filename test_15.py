'''
name? 1
age? 2
[{"name": "1", "age": "2"}]
name? 3
age? 4
[{"name": "1", "age": "2"},{"name":"3", "age": "4"}]


    {"name": "Alex", "ages": "51"},
    {"name": "Dima", "ages": "46"},
    {"name": "Olena", "ages": "49", "id":3} 
'''

# users = []
# a='2'
# while a=='2':
#     f = input('как тебя зовут ?  -  ')
#     g = input('сколько тебе лет ?  -  ')
#     user = {}
#     user["name"] = f
#     user['age'] = g
#     users.append(user)
#     print(users)
#     a = input(если хочешь продолжить, нажми '2')   

# users = []
# max=0
# while max<2:
#     max = max + 1
#     f = input('как тебя зовут ?  -  ')
#     g = input('сколько тебе лет ?  -  ')
#     user = {}
#     user["name"] = f
#     try:
#         user['age'] = int(g)
#     except:
#         print('Error!!!!!')
#     user['id'] = max
#     users.append(user)
#     print(users)

users = []
max=0
while max<2:
    max = max + 1
    user = {}
    f = input('как тебя зовут ?  -  ')
    while len(f)<2:
        print('имя короткое')
        f = input('как тебя зовут ?  -  ')    
    user['name'] = f
    flag = 0
    while flag==0:
        try:
            g = input('сколько тебе лет ?  -  ')
            user['age'] = int(g)
            flag = 1
        except:
            print('Error!!!!!')
    user['id'] = max
    users.append(user)
    print(users)
    