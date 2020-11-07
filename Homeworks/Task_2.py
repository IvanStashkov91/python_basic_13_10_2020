'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param, name='Factory'):
        self.name = name
        self.param = param

    @abstractmethod
    def abstract(self):
        pass

    @property
    def fabric_consumption(self):
        return f'Total: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f} fabrics'


class Coat(Clothes):

    def fabric_consumption(self):
        return f'To sew the coat "{self.name}" you need {self.param / 6.5 + 0.5:.2f} fabrics'

    def abstract(self):
        pass


class Suit(Clothes):

    def fabric_consumption(self):
        return f'To sew the suit "{self.name}" you need {2 * self.param + 0.3 :.2f} fabrics'

    def abstract(self):
        pass

if __name__ == '__main__':
    coat = Coat(50, 'H&M')
    costume = Suit(180, 'Mexx')
    print(coat.fabric_consumption())
    print(costume.fabric_consumption())
