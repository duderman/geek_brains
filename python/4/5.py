# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce


def generate_even_list():
  """Iterates over a list of even nums from 100 to 1000

  Yields:
      int: current num
  """
  for i in range(100, 1000):
    if i % 2 != 0:
      continue
    yield i


result = reduce(lambda a, b: a*b, generate_even_list(), 1)

print(f"Result: {result}")
