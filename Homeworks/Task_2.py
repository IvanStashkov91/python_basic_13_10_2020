'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

count_l = 0
with open('text_2.txt') as file:
    for line in file:
        count_l += 1
        count_w = 0
        for word in line.split():
            count_w += 1
        print(f'In line number {count_l} - {count_w} word(s)')
    print(f'Amount of lines in text file - {count_l} line(s)')
