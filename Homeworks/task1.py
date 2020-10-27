'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv

file_name, user_hour, user_rate, user_bonus = argv

def user_salary(work_hour, rate, bonus):
    return (int(work_hour) * int(rate)) + int(bonus)

while True:
    try:
        print(user_salary(user_hour, user_rate, user_bonus))
        break
    except ValueError:
        print('Please, enter the number!')
        break
