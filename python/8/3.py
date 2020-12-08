# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

import unittest


class NumbersOnly(Exception):
  @classmethod
  def check(cls, list):
    for n in list:
      if isinstance(n, int):
        continue

      if isinstance(n, str) and n.isdigit():
        continue

      raise cls(f"{n} is not an integer")
    return list


class TestNumbersOnly(unittest.TestCase):
  def test_check(self):
    self.assertEqual(NumbersOnly.check([1, 2, 3]), [1, 2, 3])
    self.assertEqual(NumbersOnly.check([]), [])
    self.assertRaises(NumbersOnly, NumbersOnly.check, ['a'])
    self.assertRaises(NumbersOnly, NumbersOnly.check, [1, 'b', 3])


if __name__ == '__main__':
    unittest.main()
