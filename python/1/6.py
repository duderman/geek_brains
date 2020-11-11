import sys


def ask(msg):
  try:
    n = int(input("{}: ".format(msg)))
    if n < 0:
      print("Can't do negs :(")
      sys.exit(1)
    return n
  except ValueError:
    print("Not a number")
    sys.exit(1)


a = ask("a")
b = ask("b")

if a > b:
  print("Check your data plz")
  sys.exit(1)

i = 1
c = a

while c < b:
  i += 1
  c += c * 0.1

print(i, "day")
