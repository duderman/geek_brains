# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

import unittest


class PlzNotZero(Exception):
  pass


def can_be_divided_by(x):
  try:
    if x == 0:
      raise PlzNotZero('just stop')
  except PlzNotZero:
    return False
  else:
    return True


class Test(unittest.TestCase):
  def test_can_be_divided_by(self):
    self.assertTrue(can_be_divided_by(1))
    self.assertTrue(can_be_divided_by(-1))
    self.assertFalse(can_be_divided_by(0))


if __name__ == '__main__':
    unittest.main()
