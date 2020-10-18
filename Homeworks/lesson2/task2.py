'''
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

while True:
    el_count = input('Введите количество элементов в списке:\n>>> ')
    if el_count.isdigit():
        el_count = int(el_count)
        break
    else:
        print('Ошибка ввода! Вы ввели не число')

list = []
i = 0

while i < el_count:
    list.append(input(f"Введите {i} - е значение списка:\n >>> "))
    i += 1

i = 0
if len(list) % 2 == 0:
    while i < len(list):
        el = list[i]
        list[i] = list[i+1]
        list[i+1] = el
        i += 2
else:
    while i < len(list) - 1:
        el = list[i]
        list[i] = list[i + 1]
        list[i + 1] = el
        i += 2
print(list)


