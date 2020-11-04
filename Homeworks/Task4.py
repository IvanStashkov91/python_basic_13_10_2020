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
        return f'{self.color} {self.name} drove'

    def stop(self):
        return f'{self.color} {self.name} stopped'

    def turn(self, direction):
        self.direction = direction
        return f'{self.color} {self.name} turned {self.direction}'

    def show_speed(self):
        return f'{self.color} {self.name} speed is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Over speed!!! Your speed is {self.speed}.'
        else:
            return f'The car speed is {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Over speed!!! Your speed is {self.speed}'
        else:
            return f'The car speed is {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)



if __name__ == '__main__':
    tesla = TownCar(70, 'white', 'Tesla')
    iveco = WorkCar(55, 'black', 'Iveco')
    bugatti = SportCar(150, 'black', 'Bugatti')
    toyota = PoliceCar(110, 'white-blue', 'Toyota')
    print(tesla.go())
    print(iveco.go())
    print(bugatti.go())
    print(toyota.go())
    print(toyota.turn('left'))
    print(tesla.show_speed())