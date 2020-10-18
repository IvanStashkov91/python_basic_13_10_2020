'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

while True:
    month_number = input('Введите месяц в виде целого числа:\n>>> ')
    if month_number.isdigit():
        month_number = int(month_number)
        break
    else:
        print('Ошибка ввода! Вы ввели не число')

seasons_dict = {
    'зима': (1, 2, 12),
    'весна': (3, 4, 5),
    'лето': (6, 7, 8),
    'осень': (9, 10, 11)
}

for season in seasons_dict.keys():
    if month_number in seasons_dict[season]:
        print(f'{month_number}-й месяц - {season}')



seasons_list = ['зима', 'весна', 'лето', 'осень']

if month_number == 1 or month_number == 12 or month_number == 2:
    print(f'{month_number}-й месяц - {seasons_list[0]}')
elif month_number == 3 or month_number == 4 or month_number ==5:
    print(f'{month_number}-й месяц - {seasons_list[1]}')
elif month_number == 6 or month_number == 7 or month_number == 8:
    print(f'{month_number}-й месяц - {seasons_list[2]}')
else:
    print(f'{month_number}-й месяц - {seasons_list[3]}')

