'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt

def division():
    try:
        divident = float(input('Enter divident: '))
        divider = float(input('Enter divider: '))
        if divider == 0:
            raise DivisionByZero("Can not division by zero")
        else:
            return divident / divider
    except ValueError:
        return "Not a number"
    except DivisionByZero as err:
        return err


print(division())
