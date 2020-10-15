'''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

n = input('Please, enter n number:\n>>> ')
nn = n + n
nnn = n + n + n
sum = int(n) + int(nn) + int(nnn)
print(f'The sum of the "n + nn + nnn" wil be: {sum}')
