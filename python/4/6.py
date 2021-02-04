# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle
from utils import generate_random_list


def generate_list(start, end):
  """Generates a list of numbers within a range

  Args:
      start (int): Start element
      end (int): End element

  Yields:
      int: current element
  """
  for i in count(start):
    if i == end:
      break
    yield i


def repeat_list(list, times):
  """Repeats list elements specified number of times

  Args:
      list (list): List of elements to repeat
      times (int): How many times to repeat

  Yields:
      int: Current element
  """
  i = 0
  for el in cycle(list):
    if i == times:
      break
    yield el
    i += 1


rand_list = generate_random_list(3)
generated_list = [el for el in generate_list(10, 15)]
repeated_list = [el for el in repeat_list(rand_list, 10)]

print(f"Generated: {generated_list}")
print(f"Repeated: {repeated_list}")
