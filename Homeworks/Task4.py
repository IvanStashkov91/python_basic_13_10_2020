'''
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''

def my_func1(x, y):
    return x ** y

def my_func2(x, y):
    if y == 0:
        return 1
    if y == -1:
        return 1 / x
    result = my_func2(x, y // 2)
    result *= result
    if y % 2:
        result *= x
    return result

while True:
    try:
        number1 = float(input('Please, enter real positive number:\n>>> '))
        number2 = int(input('Please, enter integer negative number:\n>>> '))
        if number1 > 0 and number2 < 0:
            print(my_func1(number1, number2))
            print(my_func2(number1, number2))
        else:
            print('Enter the real positive first number and integer negative second one')
    except ValueError:
        print('Please, enter the number!')
