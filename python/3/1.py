from utils import ask_int

def div(a, b):
  """
  Divides a by b
  """
  return a / b


a = ask_int('a')
b = ask_int('b')

try:
  result = div(a, b)
  print(f"Result: {result}")
except ZeroDivisionError:
  print("Can't divide by 0")
