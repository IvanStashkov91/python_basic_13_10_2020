'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''

number = int(input('Введите натуральное число:\n>>> '))
list = [9, 7, 5, 4, 2, 1]
count = list.count(number)
for element in list:
    if count > 0:
        index = list.index(number)
        list.insert(index + count, number)
        break
    else:
        if number > element:
            index = list.index(element)
            list.insert(index, number)
            break
        elif number < list[len(list) - 1]:
            list.append(number)
print(list)
