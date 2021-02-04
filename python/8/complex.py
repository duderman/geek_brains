# 7. Реализовать проект «Операции с комплексными числами».
#
# Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

import unittest


class Complex():
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def __str__(self):
    result = ''
    if self.a != 0:
      result += f"{self.a} "

    if self.b < 0:
      result += '-'
    elif self.a != 0:
      result += '+'

    result += ' '

    if abs(self.b) != 1:
      result += str(abs(self.b))

    result += 'i'

    return result

  def __add__(self, other):
    return Complex(self.a + other.a, self.b + other.b)

  def __mul__(self, other):
    new_a = self.a * other.a - self.b * other.b
    new_b = self.a * other.b + self.b * other.a
    return Complex(new_a, new_b)


class Test(unittest.TestCase):
  def test_add(self):
    z1 = Complex(1, 3)
    z2 = Complex(4, -5)
    self.assertEqual(str(z1 + z2), '5 - 2i')

  def test_mul(self):
    z1 = Complex(2, 3)
    z2 = Complex(-1, 1)
    self.assertEqual(str(z1 * z2), '-5 - i')


if __name__ == '__main__':
    unittest.main()
