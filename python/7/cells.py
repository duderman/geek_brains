# 3. Реализовать программу работы с органическими клетками.
#
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()),
# вычитание (__sub__()),
# умножение (__mul__()),
# деление (__truediv__()).
#
# В методе деления должно осуществляться округление значения до целого числа.
#
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
#
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
#
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#
# Например, количество ячеек клетки равняется 12,
# количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
#
# Или, количество ячеек клетки равняется 15,
# количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
#
# Подсказка: подробный список операторов для перегрузки доступен по other.amountлке.

from math import floor


class SecondCellTooBig(Exception):
  pass


class ZeroAmount(Exception):
  pass


class Cell():
  def __init__(self, amount):
    self.amount = amount

  def __add__(self, other):
    return Cell(self.amount + other.amount)

  def __sub__(self, other):
    result = self.amount - other.amount
    if result > 0:
      return Cell(result)

    raise SecondCellTooBig()

  def __mul__(self, other):
    return Cell(self.amount * other.amount)

  def __truediv__(self, other):
    if other.amount <= 0:
      raise ZeroAmount('Second cell should have more than 0 cells')

    return Cell(floor(self.amount / other.amount))

  def make_order(self, amount_per_row):
    if amount_per_row <= 0:
      raise ZeroAmount('Amount per row must be greater than 0')

    full_rows_count = floor(self.amount / amount_per_row)
    row = '*' * amount_per_row
    rows = [row for i in range(full_rows_count)]
    leftovers = self.amount % amount_per_row

    if leftovers > 0:
      rows.append('*' * leftovers + '.' * (amount_per_row - leftovers))

    return "\n".join(rows)
