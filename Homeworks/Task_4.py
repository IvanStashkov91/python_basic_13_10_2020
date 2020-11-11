'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
'''

class Store:

    def __init__(self, name):
        self.name = name
        self.equipment = {}

    def add_office_equipment(self, unit,  equipment, amount):
        if not isinstance(equipment, OfficeEquipment):
            raise ValueError('Incorrect equipment')
        self.equipment.setdefault(unit, []).extend([equipment, amount])

    def __str__(self):
        return str(self.equipment)

class OfficeEquipment:
    def __init__(self, name, i_d, price, quantity):
        self.name = name
        self.i_d = i_d
        self.price = price
        self.quantity = quantity


class Printer(OfficeEquipment):
    def __init__(self, name, i_d, price, quantity,  color):
        super().__init__(name, i_d, price, quantity)
        self.__color = color


class Scanner(OfficeEquipment):
    def __init__(self, name, i_d, price, quantity,  color, quality):
        super().__init__(name, i_d, price, quantity)
        self.color = color
        self.quality = quality


class Xerox(OfficeEquipment):
    def __init__(self, name, i_d, price, quantity,  color, format):
        super().__init__(name, i_d, price, quantity)
        self.color = color
        self.format = format


if __name__ == '__main__':
    printer = Printer('Samsung', 45657586, 150, 5, 'Black-white')
    scanner = Scanner('HP', 546579, 200, 1, 'Color', 'High quality')
    xerox = Xerox('Samsung', 9567889, 100, 1, 'Black-white', 'A-4')

    stock = Store('Apple')
    stock.add_office_equipment('Unit of development', printer, 4)
    stock.add_office_equipment('Store', scanner, 2)
    stock.add_office_equipment('HR', xerox, 5)
