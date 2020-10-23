'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
'''

def my_func(x, y, z):
    if x >= z and y >= z:
        return x + y
    elif x >= y and z >= y:
        return x + z
    elif y >= x and z >= x:
        return y + z

while True:
    try:
        number1 = float(input('Please, enter first argument:\n>>> '))
        number2 = float(input('Please, enter second argument:\n>>> '))
        number3 = float(input('Please, enter third argument:\n>>> '))
        print(my_func(number1, number2, number3))
        break
    except ValueError:
        print('Please, enter the number!')
