'''
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и
словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
'''

products = []
product_features = {'Название': '', 'Цена': '', 'Количество': '', 'ед.': ''}
product_analytics = {'Название': [], 'Цена': [], 'Количество': [], 'ед.': []}
num = 0
while True:
    move = input("Чтобы продолжить, нажмите 'Enter'. Для выхода нажмите 'Q'. Чтобы посмотреть аналитику нажмите 'A'").upper()
    if move == 'Q':
        break
    num += 1
    if move == 'A':
        for key, value in product_analytics.items():
            print(f'{key}:{value}')
    for keys in product_features.keys():
        feature = input(f'Введите "{keys}" ')
        product_features[keys] = int(feature) if (keys == 'Цена' or keys == 'Количество') else feature
        product_analytics[keys].append(product_features[keys])
    products.append((num, product_features))
