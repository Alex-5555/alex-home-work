'''

Alex - 51
-- Ann
-- Anastasia

Dima - 47

Aloyna - 49
'''
users = [
    {"name": "Alex", "age": 51, "kids": [
        {"name_1": "Ann"},
        {"name_1": "Anastasia"}]
    },
    {"name": "Dima", "age": 47, "kids": [
        {"name_1": "Bogdan"},
        {"name_1": "Lyova"}]},
    {"name": "Alyona", "age": 49, "kids": [
        {"name_1": "Ket"},
        {"name_1": "Lisa"}]}
]
for user in users:
    print(f'{user["name"]} - {user["age"]}', end='')
    for kid in user["kids"]:
        print("--" + kid["name_1"], end='')
    print(' ')