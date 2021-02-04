# 4. Начните работу над проектом «Склад оргтехники».
#
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class NoUnitsLeft(Exception):
  pass

class Warehouse():
  def __init__(self):
    self.units = {}

  def add_unit(self, unit):
    unit_type = type(unit)
    self.units.setdefault(unit_type, [])
    self.units[unit_type].append(unit)

  def give_unit_of_type(self, unit_type):
    if self._is_all_gone(unit_type):
      raise NoUnitsLeft(f"No {unit_type} units left")

    return self.units[unit_type].pop()

  def _is_all_gone(self, unit_type):
    return not unit_type in self.units.keys() or len(self.units[unit_type]) == 0


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
