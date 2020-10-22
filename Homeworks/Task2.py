'''2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def user_data(**kwargs):
    return list(kwargs.values())

print(user_data(name= input('Please, enter your name:\n>>> '),
                sirname = input('Please, enter your sirname:\n>>> '),
                year = input('Please, enter your birth year:\n>>> '),
                city = input('Please, enter your residence city:\n>>> '),
                e_mail = input('Please, enter your e-mail:\n>>> '),
                tel_numb = input('Please, enter your telephone number:\n>>> ')))
