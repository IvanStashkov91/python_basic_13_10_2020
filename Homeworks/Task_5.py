'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
import function_list

with open('text_5.txt', 'w', encoding='UTF-8') as file:
    line = input('Write the numbers through space:\n>>> ')
    file.writelines(line)
with open('text_5.txt', 'r', encoding='UTF-8') as file:
    n = file.read().split()
    for i in range(len(n)):
        n[i] = float(n[i])
    print(f'Sum of numbers in "text_5.txt": {function_list.my_sum(n)}')
