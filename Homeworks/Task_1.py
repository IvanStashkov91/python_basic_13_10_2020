'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

with open('text_1.txt', 'w', encoding='UTF-8') as file:
    while True:
        line = input('Write the line or press "Enter" to stop:\n>>> ')
        if not line:
            break
        file.writelines(line + '\n')
