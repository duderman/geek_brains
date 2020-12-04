# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():
  """
  Represents a stationary item
  """

  def __init__(self, title):
    self.title = title

  def draw(self):
    """
    Draw something with an item
    """
    return 'Starting to draw'


class Pen(Stationery):
  """
  A pen class
  """

  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    return 'Drawing with a pen'


class Pencil(Stationery):
  """
  A pencil class
  """

  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    return 'Drawing with a pencil'


class Handle(Stationery):
  """
  A handle class
  """

  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    return 'Drawing with a handle'
