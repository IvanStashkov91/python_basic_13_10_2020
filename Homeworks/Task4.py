'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_possible = is_police

    def go(self):
        print(f'{self.color} {self.name} drove')

    def stop(self):
        print(f'{self.color} {self.name} stopped')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.color} {self.name} turned {self.direction}')

    def show_speed(self, speed):
        self.speed = speed
        print(f'{self.color} {self.name} speed is {self.speed}')

class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if speed > 60:
            print(f'Over speed!!! Your speed is {speed}')
        else:
            print(f'The car speed is {speed}')

class SportCar:
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar:
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if speed > 60:
            print(f'Over speed!!! Your speed is {speed}')
        else:
            print(f'The car speed is {speed}')

class PoliceCar:
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)







