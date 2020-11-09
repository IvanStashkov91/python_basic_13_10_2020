'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

from datetime import date

class Data:
    def __init__(self, d_m_y):
        self.d_m_y = d_m_y

    @classmethod
    def extraction_d_m_y(cls, d_m_y):
            day, month, year = d_m_y.split('-')
            for itm in d_m_y.split('-'):
                if (0 < int(day) < 32) and (0 < int(month) < 13):
                    return f'{day}, {month}, {int(year)}'
                else:
                    return f'Incorrect date'

    @staticmethod
    def validation_d_m_y(d_m_y):
        try:
            day, month, year = d_m_y.split('-')
            date(int(year), int(month), int(day))
            return f'Correct date'
        except ValueError:
            return f'Incorrect date'

if __name__ == '__main__':
    print(Data.extraction_d_m_y('02-98-90'))
    print(Data.validation_d_m_y('1-1-1'))






