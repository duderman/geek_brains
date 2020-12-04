# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class WrongSize(Exception):
  pass

class Matrix():
  """
  Matrix class
  """

  def __init__(self, values):
    for list in values[1:]:
      if len(list) != len(values[0]):
        raise WrongSize()
    self.values = values

  def __str__(self):
    if len(self.values) == 0:
      return ''

    result = ['⌈ ' + ' '.join(map(str, self.values[0])) + ' ⌉']
    for list in self.values[1:-2]:
      vals = map(str, list)
      result.append('| ' + ' '.join(vals) + ' |')
    result.append('⌊ ' + ' '.join(map(str, self.values[-1])) + ' ⌋')

    return "\n".join(result)

  def __add__(self, other):
    result = []
    for n in range(len(self.values)):
      result.append([self.values[n][m] + other.values[n][m]
                     for m in range(len(self.values[n]))])
    return Matrix(result)
