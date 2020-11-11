import sys

try:
  total = int(input("seconds: "))
except ValueError:
  print("Not a number")
  sys.exit(1)

if total < 0:
  print("Can't do negs :(")
  sys.exit(1)


def hours(total):
  return round(total / 3600)


def minutes(total):
  wo_hours = total % 3600
  return round(wo_hours / 60)


def seconds(total):
  return total % 3600 % 60


def to_hhmmss(total):
  h = hours(total)
  m = minutes(total)
  s = seconds(total)

  return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


print(to_hhmmss(total))
