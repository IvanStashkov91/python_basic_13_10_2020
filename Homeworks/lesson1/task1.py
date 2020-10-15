'''
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
и строк и сохраните в переменные, выведите на экран.
'''

name = 'Ivan'
age = 29
height = 180
weight = 72.3
city_name = 'Krasnoyarsk'
friends_name = ['Ivan', 'Andrey', 'Nikolay']

print(name)
print(age, 'year')
print(height, 'sm')
print(weight, 'kg')
print(city_name)
print(friends_name)

name_request = input('Пожалуйста, введите свое имя:\n>>>')
age_request = input('Пожалуйста, введите свой возраст:\n>>>')
weight_request = input('Пожалуйста, введите свой вес:\n>>>')
city_request = input('Пожалуйста, напишите город в котором вы проживаете:\n>>>')

print(name_request)
print(age_request)
print(weight_request)
print(city_request)

print(f'Привет.\nВас зовут {name_request}, вам {age_request} лет.\nМасса вашего тела составляет {weight_request} килограмм.\nВы проживаете в городе {city_request}.')
