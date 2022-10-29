import random

# bank = 0
users = [
            {"name": "Alex", "pocket": 10}, 
            {"comp": "Dells", "pocket": 10}
]

stop = 'yes'
all = [1]
while min(all) > 0:
    alex_point = random.randint(1,11)
    comp_point = random.randint(1,11)
    if alex_point>comp_point:
        print(f'Alex won!!! {alex_point}={comp_point}')
        users[0]["pocket"] -=1
        users[1]["pocket"] +=1
    else:
        print(f'Comp won!!! {alex_point}={comp_point}')
        users[1]["pocket"] -=1
        users[0]["pocket"] +=1
    print(users)    
    stop = input('one more time? - ')
    
    if len(stop) == 0:
        stop = 'yes'
    for u in users:
        all.append(u["pocket"])