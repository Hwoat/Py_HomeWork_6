'''
Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который
должен показывать текущую скорость автомобиля. Для классов TownCar
и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} запущена'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} равна {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость класса town car {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Скорость  {self.name} выше, чем разрешенная для класса town car'
        else:
            return f'Скорость {self.name} нормальная для  town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость класса work car {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше, чем ращрешенная для класса work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} не из полиции'



oka = TownCar(30, 'Белый', 'Ока', False)
volvo = SportCar(100, 'Красный', 'Volvo', False)
lada = WorkCar(70, 'Желтый', 'Лада', True)
toyota = PoliceCar(110, 'Синий',  'Toyota', True)
print(lada.turn_left())
print(f'{lada.go()} со скоростью {lada.show_speed()}')
print(f'{lada.name} - {lada.color}')
print(f' {volvo.name} из полиции? {volvo.is_police}')
print(volvo.show_speed())
print(oka.show_speed())
print(toyota.police())
print(toyota.show_speed())