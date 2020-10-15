'''
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составил не менее b километров.
Программа должна принимать значения параметров a и b, и выводить одно натуральное число — номер дня.
'''

a = float(input('How many kilometers did you run in first day:\n>>> '))
b = float(input('How many kilometers did you run in these days:\n>>> '))
percent = 0.1

day_number = 1
while a < b:
    a = a * (1 + percent)
    day_number += 1
print(f'The result will be {a:.2f} kilometers')
print(f'In the {day_number} day the athlete achived a result of at least {b} kilometers')
