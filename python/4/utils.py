import random

DEFAULT_LIST_LENGTH = 10
MIN_RAND_NUM = 1
MAX_RAND_NUM = 100


def generate_random_list(length=DEFAULT_LIST_LENGTH, min=MIN_RAND_NUM, max=MAX_RAND_NUM):
  """Generates a list of random numbers

  Args:
      length (int, optional): desired list length. Default: 10
      min (int, optional): min random number. Default: 1
      max (int, optional): max random number. Default: 100

  Raises:
      ValueError: when length is less or equal to zero

  Returns:
      list: list of random numbers
  """
  if length < 1:
    raise ValueError('length must be greater than 0')

  list = []
  for _ in range(length):
    n = random.randint(min, max)
    list.append(n)

  return list
