'''some_variable = 1

mass: float = 22.345
street_name = 'Lenina'

mass2 = 344.55

mass3 = mass + mass2 # тип переменной float
mass4 = some_variable + mass2 # тип переменной float'''

#this_year = 2020
#name = input('Your name\n>>>: ') #тип данных всегда строка
#surname = input('Your sirname\n>>>: ')
#age = int(input('Your age\n>>> '))

#ful_user_data1 = f'user {name} {surname} {this_year - int(age)} year'
#ful_user_data = f'user \n {name:>20}\n{surname:<20}\n{this_year - int(age):^20}\nyear' #редоктирование по левому краюб центруб правому краю

#print(ful_user_data1)
#print(ful_user_data)
#b_one = True
#b_two = False

#if age >= 18:  # сдесь пишется утверждение
   # print('accses')
  #  if age > 30:
      #  print('Пока все дома')
#elif age >= 16:
   # print('доступ к конткнту 16+')
#elif age < 12:
   # print('Можно смотреть мультики')
#else:
    #print('No')


'''
if
elif
else
in
>
<
>=
<=
!=
not
and
or
'''
#введение только чисел цифрами
while True:
    user_a = input('введите целое число результата в первый день\n')
    if user_a.isdigit():
        user_a = int(user_a)
        break
    else:
        print('ошибка ввода, это не число')