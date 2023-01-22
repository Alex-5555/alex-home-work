from collections import Counter 
'''
s = 'Голова думала'
def top3(st):
    counter_top3 = Counter(st.replace(' ', '')).most_common(3)
    return ', '.join([f'{letter} - {num}' for letter, num in counter_top3])
print(top3(s))

def search_substr(subst, st):
    res = st.find(subst)
    if res >=0:
        return 'Есть контакт'
    else:
        'Мимо'
print(search_substr('bara', 'baraban'))

def search_substr(subst, st):
    if subst.lower() in st.lower():
        return 'Есть контакт'
    else:
        'Мимо'
print(search_substr('bara', 'baraban'))

def first_last(letter, st):
    g = st.find(letter)    
    f =  st.rfind(letter)
    if g < 0:
        return None, None
    else:   
        return g, f
print(first_last('c', 'baraban'))

def camel(st):
    camel_st = ''
    counter = 0
    for index, val in enumerate(st):
        if val.isalpha():
            if counter % 2 == 0:
                camel_st += val.upper()
            else:
                camel_st += val.lower()
            counter += 1
        else:
            camel_st += val
    return camel_st
print(camel('Голова! думала!'))

def shortener(st):
    while '(' in st or ')' in st:
        left = st.rfind('(')
        print(left)
        right = st.find(')', left)
        print(right)
        st = st.replace(st[left: right + 1], '')
        print(st)
    return st
print(shortener('Падал(лишнее (лишнее) лишнее) прошлогодний снег (лишнее)'))
'''
def cleaned(st):
    clean_st = []
    for simbol in st:
        if simbol == '@' and clean_st:
            clean_st.pop()
        elif simbol != '@' and simbol.isalpha():
            clean_st.append(simbol)
    return ''.join(clean_st)
print(cleaned('гр@оо@л.к@23оц@ва'))

    

