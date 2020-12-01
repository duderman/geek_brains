# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road():
  """
  Describes road work
  """

  SQUARE_METER_MASS = 25
  HEIGHT = 5

  def __init__(self, length, width):
    self.__length = length
    self.__width = width

  def concrete_total(self):
    """
    Calculates required concrete amount
    """
    return self.__width * self.__length * self.SQUARE_METER_MASS * self.HEIGHT


road = Road(5000, 20)
print(road.concrete_total())
