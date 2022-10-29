from curses import mousemask
from itertools import count
import random

x = 2
xx = 10
bank = x + x
ff = input('как тебя зовут ? - ')
ff_1 = input(f'У тебя {xx} грн., шаг игры {x} грн.')
users = [
         {"name": ff, "pocket": 10}, 
         {"comp": "Dells", "pocket": 10}
         ]

all = [1]
while min(all) > 0:  
    faces = ['clubs', 'heart', 'diamond', 'spade']
    ranks = ['6','7','8','9','10','A']
    koloda = []
    for face in faces:
        for rank in ranks:
            if rank=='6':
                n = 6
            if rank=='7':
                n = 7
            if rank=='8':
                n = 8
            if rank=='9':
                n = 9
            if rank=='10':
                n = 10
            if rank=='A':
                n = 11
            koloda.append({'face': face, 'rank': rank, 'count': n})
    # print(koloda)
    random.shuffle(koloda)
    
    # bank = 2
    mani_1 = input(f'чтобы начать Вами внесено в банк {x} грн.')
    users[0]['pocket'] = users[0]['pocket'] - x
    print(f"у Вас осталось {users[0]['pocket']} грн.")

    mani_comp = input(f'компьютером внесено в банк {x} грн. - для продолжения нажми enter')
    users[1]['pocket'] = users[1]['pocket'] - x
    print(f"у компьютера осталось {users[1]['pocket']} грн.")
    # print(users)

    player_1 = []
    face_1 = []
    rank_1 = []
    count_1 = [] 
    monitor_1 = []
    counter = 0
    input('чтобы получить карту нажми enter - ')
    while counter<3:
        counter = counter + 1
        a = koloda.pop()
        # print(a)
        face_1.append(a['face'])
        # print(face_1)
        rank_1.append(a['rank'])
        # print(rank_1)
        count_1.append(a['count'])
        # print(count_1)
        player_1.append(a)
        # print(player_1)
        monitor_1.append(f'{a["face"]}-{a["rank"]}')    
    print(monitor_1)
    res = input(ff+' хочешь подсчитать результат ? нажми ent- ') 

    d = {}
    for i in set(face_1):
        d[i]=0
    # print(d)
    for i in player_1:
        d[i['face']] = d[i['face']] + i['count']
        # print(d)

    ii = []
    for a in faces:
        ii.append(d.get(a,0))
    s = max(ii)
    print(s)

    player_comp = []
    face_comp = []
    rank_comp = []
    count_comp = [] 
    monitor_comp = []
    fff = input('раздать карты компьютеру, не показывая результат - нажми enter')
    counter = 0
    while counter<3:
        counter = counter + 1
        aa = koloda.pop()
        # print(aa)
        face_comp.append(aa['face'])
        # print(face_comp)
        rank_comp.append(aa['rank'])
        # print(rank_comp)
        count_comp.append(aa['count'])
        # print(count_comp)
        player_comp.append(aa)
        # print(player_comp)
        monitor_comp.append(f'{aa["face"]}-{aa["rank"]}')    
        # print(monitor_comp)

    dd = {}
    for i in set(face_comp):
        dd[i]=0
        # print(dd)
    for i in player_comp:
        dd[i['face']] = dd[i['face']] + i['count']
        # print(dd)

    iii = []
    for i in faces:
        iii.append(dd.get(i,0))
    ss = max(iii)
    # print(ss)

            # alex_point = s
            # comp_point = ss
    if s<14:
        print(ff+' упал')
        print('выиграл компьютер')
        users[1]["pocket"] +=bank
        # users[0]["pocket"] -=x
        print(users)
    else:
        print(ff+' увеличил банк')
        users[0]['pocket'] = users[0]['pocket'] - x
        bank_1 = bank + x
        print('компьютер упал')
        print(ff+' выиграл')
        users[0]["pocket"] +=bank_1
        # users[1]["pocket"] -=x
        print(users)
    all = [users[1]["pocket"], users[0]["pocket"]]

stop = 'yes'
all = [1]
while min(all) > 0:      
    if len(stop) == 0:
        stop = 'yes'
    for u in users:
        all.append(u["pocket"])   
        print(all) 
