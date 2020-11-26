from utils import ask_int


def my_func(a, b):
  """
  Returns a powered by b
  """
  result = 1
  for i in range(-b):
    result = result / a

  return result


a = ask_int('a', lambda n: n > 0, 'Must be positive')
b = ask_int('b', lambda n: n < 0, 'Must be negative')
result = my_func(a, b)

print(f"Result {result}")
