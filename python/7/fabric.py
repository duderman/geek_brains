# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани.
#
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABCMeta, abstractmethod


class Cloth(metaclass=ABCMeta):
  @abstractmethod
  def fabric_amount(self):
    pass

  @staticmethod
  def fabric_total(clothes):
    return sum([cloth.fabric_amount() for cloth in clothes])


class Coat(Cloth):
  def __init__(self, size):
    super().__init__()
    self._size = size

  @property
  def size(self):
    return self._size

  def fabric_amount(self):
    return self._size / 6.5 + 0.5


class Suit(Cloth):
  def __init__(self, height):
    super().__init__()
    self._height = height

  @property
  def height(self):
    return self._height

  def fabric_amount(self):
    return self._height * 2 + 0.3
