'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу.
'''

# Код можно сократить если использовать ф-ю sum(), но не смог ее вставить корректно
def sum(list):
    result = 0
    for itm in list:
        result = result + int(itm)
    return result

try:
    sum = 0
    while True:
        number_list = input('Enter a string of numbers separated by space.\nEnter "#" to finish the programm.\n>>> ').split()
        if '#' in number_list:
            number_list = number_list[:number_list.index('#')]
            for item in number_list:
                sum += int(item)
            print(sum)
            break
        else:
            for item in number_list:
                sum += int(item)
            print(sum)
except ValueError:
        print('You did not enter number. Enter a string of numbers separated by space.\nEnter "#" to finish the programm')
