"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = int(input('Plese, enter a positive integer:\n>>> '))
first_number = number
max = 0
while number > 10:
    max_number = number % 10
    number //= 10
    if max_number >= max:
        max = max_number

print(f'Maximum digit of number {first_number} is {max}.')
