# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

def __fact(n, curr, i):
  if i > n:
    return

  next = curr * i
  yield next
  yield from __fact(n, next, i + 1)


def fact(n):
  """Iterates over factorials

  Args:
      n (int): Number of factorials

  Yields:
      int: Current factorial
  """
  yield from __fact(n, 1, 1)


facts = [el for el in fact(5)]

print(f"Factorials: {facts}")
