'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('text_3.txt', 'r', encoding='UTF=8') as file:
    salary = []
    sum = 0
    count = 0
    for line in file.readlines():
        line = line.split()
        sum += int(line[1])
        count += 1
        if int(line[1]) < 20000:
            salary.append(line[0])
    print(f'{salary} have a salary less then 20000')
    print(f'Average employee income is {sum / count}')
