'''
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

revenue = float(input('Enter a revenue of your company, $:\n>>> '))
costs = float(input('Enter a company costs, $:\n>>> '))

if revenue > costs:
    profit = revenue - costs
    print(f'The company is in profit. Revenue profitability is {profit / revenue:.2f}')
    staff = int(input('Enter the number of company employees:\n>>> '))
    print(f'Company profit per employee is {profit / staff:.2f}')
elif revenue == costs:
    print('The company does not get income')
else:
    print('The company operates at a loss')
