# Начните работу над проектом «Склад оргтехники».
#
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse():
  pass


class Unit():
  def __init__(self, manufacturer, model):
    self.manufacturer = manufacturer
    self.model = model


class Printer(Unit):
  def __init__(self, manufacturer, model, color):
    super().__init__(manufacturer, model)
    self.color = color


class Display(Unit):
  def __init__(self, manufacturer, model, inches):
    super().__init__(manufacturer, model)
    self.inches = inches
