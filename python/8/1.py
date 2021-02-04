# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#
# Проверить работу полученной структуры на реальных данных.

import unittest
import re


class IncorrectFormat(Exception):
  pass


class InvalidDate(Exception):
  pass


class Date():
  date_re = re.compile('\d{2}-\d{2}-\d{4}')
  max_days_in_months = [31, 29, 31, 30, 31, 30,   31, 31, 30, 31, 30, 31]

  def __init__(self, date_string):
    if not self.date_re.match(date_string):
      raise IncorrectFormat('Date must be in format dd-mm-yyy')

    self.date_string = date_string

  def to_ints(self):
    return [int(part) for part in self.date_string.split('-')]

  @classmethod
  def parse_and_convert_to_ints(cls, date_string):
    return cls(date_string).to_ints()

  @staticmethod
  def validate(date_string):
    day, month, year = Date.parse_and_convert_to_ints(date_string)
    if month < 1 or month > 12:
      raise InvalidDate('Month should be within 1 to 12 range')
    if day < 1:
      raise InvalidDate('Day must be greater than 1')
    max_days_in_month = Date.max_days_in_months[month - 1]
    if day > max_days_in_month:
      raise InvalidDate(
          f"Month {month} can have up to {max_days_in_month} days")
    if month == 2 and not year % 4 == 0 and day > 28:
      raise InvalidDate(f"Feb in not a leap year can't have more than 28 days")

    return True


class TestDate(unittest.TestCase):
  def test_init(self):
    date = Date('10-01-1991')
    self.assertEqual(date.date_string, '10-01-1991')

  def test_init_with_invalid_date(self):
    self.assertRaises(IncorrectFormat, Date, 'asd')

  def test_parse_and_convert_to_ints(self):
    day, month, year = Date.parse_and_convert_to_ints('10-01-1991')
    self.assertEqual(day, 10)
    self.assertEqual(month, 1)
    self.assertEqual(year, 1991)

  def test_validate(self):
    self.assertRaises(InvalidDate, Date.validate, '10-22-1991')
    self.assertRaises(InvalidDate, Date.validate, '10-00-1991')
    self.assertRaises(InvalidDate, Date.validate, '00-01-1991')
    self.assertRaises(InvalidDate, Date.validate, '32-01-1991')
    self.assertRaises(InvalidDate, Date.validate, '31-04-1991')
    self.assertRaises(InvalidDate, Date.validate, '29-02-1991')
    self.assertTrue(Date.validate('29-02-2016'))


if __name__ == '__main__':
    unittest.main()
