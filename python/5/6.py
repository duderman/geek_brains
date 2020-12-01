from re import findall
from functools import reduce


def get_hours_sum(hours_str):
  return reduce(lambda a, b: a + int(b), findall(r"\d+", hours_str), 0)


classes = {}

with open('classes.txt') as file:
  for line in file:
    class_name, hours = line.split(': ')
    hours_sum = get_hours_sum(hours)
    classes[class_name] = hours_sum

print(f"Result: {classes}")
