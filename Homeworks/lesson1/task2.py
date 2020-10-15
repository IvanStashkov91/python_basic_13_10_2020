'''
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''
# todo первый вариант
time_seconds = int(input('Please, enter your time in sec::\n>>>'))
hours = time_seconds // 3600
minutes = (time_seconds - hours * 3600) // 60
seconds = time_seconds - (hours * 3600 + minutes * 60)
print(f"The time in 'hh.mm.ss' format is: {hours}:{minutes}:{seconds}")

# todo второй вариант
time_seconds = int(input('Please, enter your time in sec::\n>>>'))
hours = time_seconds // 3600
remain = time_seconds % 3600
minutes = remain // 60
seconds = remain % 60
print(f"The time in 'hh.mm.ss' format is: {hours}:{minutes}:{seconds} ")

# todo третий вариант
time_seconds = int(input('Please, enter your time in sec::\n>>>'))
remain = time_seconds % 3600
print(f"The time in 'hh.mm.ss' format is: {time_seconds // 3600}:{remain // 60}:{remain % 60} ")
