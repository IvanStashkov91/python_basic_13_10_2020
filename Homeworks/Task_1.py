'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def division(arg1, arg2):
        try:
            return arg1 / arg2
        except ZeroDivisionError:
            return 'Can not divide by zero'
        except ValueError:
            return 'ValueError'

while True:
    try:
        a = float(input('Please, enter dividend:\n>>> '))
        b = float(input('Please, enter divider:\n>>> '))
        print(division(a,b))
        break
    except ValueError:
        print('Please, enter the number!')
