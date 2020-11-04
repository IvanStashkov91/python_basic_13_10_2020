'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Draw starting'


class Pen(Stationery):

    def draw(self):
        super().draw()
        return f'Try to use {self.title} for writing, not for drawing'


class Pencil(Stationery):

    def draw(self):
        super().draw()
        return f'Ok, it\'s great idea to use {self.title} for drawing'


class Handle(Stationery):

    def draw(self):
        super().draw()
        return f'Hmm, {self.title}. Interesting choice.'


if __name__ == '__main__':
    pen = Pen('Pen')
    pencil = Pencil('Pencil')
    handle = Handle('Handle')
    print(pen.draw())
    print(pencil.draw())
    print(handle.draw())
