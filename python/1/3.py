import sys

try:
  n = int(input("n: "))
except ValueError:
  print("Not a number")
  sys.exit(1)

if n < 0:
  print("Can't do negs :(")
  sys.exit(1)

if n > 9:
  print("Too much bruv :(")
  sys.exit(1)

print(n + 11*n + 111*n)
