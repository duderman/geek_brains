import itertools
import math


def swap(list, index):
  tmp = list[index + 1]
  list[index + 1] = list[index]
  list[index] = tmp


list = input('list: ').split()

iterations = math.floor(len(list) / 2)

for i in range(iterations):
  swap(list, i*2)

print(list)
