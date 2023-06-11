print('Address book')
print('Введите имя')
name = input()
print('Введите емейл')
email = input()
print('Введите телефон')
phone = input()
file = open('data.txt','a')
payload = '''
    Имя: %s
    Емейл: %s
    Телефон: %s
''' % (name, email, phone)
file.write(payload)
file.close()
print('Спасибо. Данные сохранены.')
file = open('data.txt','r')
print(file.read())
