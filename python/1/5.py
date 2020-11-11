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


income = ask('income')
costs = ask('costs')

if income <= costs:
  print("Loosers gonna loose")
  sys.exit(1)

earned = income - costs
print("Great job! You earned ￡{:02d}. Keep it up".format(earned))

employees = ask("Employees count")

print("Turns out each employee got around ￡{:02d}".format(
    round(earned / employees)))
