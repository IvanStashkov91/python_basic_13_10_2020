'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
from googletrans import Translator

translator = Translator()

with open('text_4_eng.txt', 'r', encoding='UTF-8') as file:
    translation = translator.translate(file.read(), dest='ru', src='en')
    with open('text_4_ru.txt', 'w', encoding='UTF-8') as file:
        file.write(translation.text)
