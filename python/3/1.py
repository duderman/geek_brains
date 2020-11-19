def div(a, b):
  """
  Divides a by b
  """
  return a / b


def ask(what):
  while True:
    try:
      return int(input(f"{what}: "))
    except ValueError:
      print("Not a number")


a = ask('a')
b = ask('b')

try:
  result = div(a, b)
  print(f"Result: {result}")
except ZeroDivisionError:
  print("Can't divide by 0")
