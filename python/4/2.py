# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from utils import generate_random_list

list = generate_random_list()
lower_list = [list[i] for i in range(1, len(list)) if list[i] < list[i - 1]]

print(f"Original list: {list}")
print(f"Calculated list: {lower_list}")
