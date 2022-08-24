questions = [
    {
        "text": "what is 2 + 2",
        "answer": 4
    },
    {
        "text": "what is 7 + 2",
        "answer": 9
    }
]

# извлечь из списка questions элемент с ключом "text"
for item in questions:
#  вывести  элемент с ключом "text" на экран 
    input_a = input(item["text"] + '    введите свой  ответ    ')
#  вывести  элемент с ключом "answer" на экран     
    num = item["answer"]
# сравниваем ответ пользователя с правильным
    if int(input_a) == num:
        print('Вы ответили правильно !')
    else:
        print('Шура, Вы дурак !')
