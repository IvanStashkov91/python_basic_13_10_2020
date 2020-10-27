'''
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка:  использовать функцию reduce().
'''

from function_list import (
    my_range,
    my_reduce,
)

list = [el for el in my_range(100, 1001, 2)]

print(f'The list of numbers from 100 to 1000 (including):\n {list}')

list_sum = my_reduce(lambda x, y: x * y, list)

print (f'The composition of numbers in "list":\n{list_sum}')
