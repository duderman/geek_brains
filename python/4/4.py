# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
#
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#
# Результат: [23, 1, 3, 10, 4, 11]

from utils import generate_random_list


def count_numbers(list):
  """Calculates numbers appearance count in a given list

  Args:
      list (list): list in which to count

  Returns:
      dict: dictionary with numbers as keys and appearance count as values
  """
  result = {}

  for el in list:
    result.setdefault(el, 0)
    result[el] += 1

  return result


list = generate_random_list(20, max=10)
counts = count_numbers(list)
uniq = [el for el, count in counts.items() if count == 1]

print(f"Original: {list}")
print(f"Uniq: {uniq}")
