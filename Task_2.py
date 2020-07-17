'''
# ------------------------------------2-----------------------------
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании
экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной
в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

  #  def canvas(self):
  #      return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume, thick):
        super().__init__(_length, _width)
        self.volume = volume
        self.thick = thick


    def mass(self):
        a = self._length * self._width * self.volume * self.thick
        print(f'Масса асфальта равна 'f'{a / 1000}')

r = MassCount(20, 5000, 25, 5)
r.mass()
