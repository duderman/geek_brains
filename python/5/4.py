from io import StringIO

NUMBERS = {
    'One': 'Раз',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семъ',
    'Eight': 'Восемъ',
    'Nine': 'Девять'
}
DELIMETER = ' - '

new_content = StringIO()

with open('numbers.txt') as file:
  for line in file:
    if not line:
      continue

    name, num = line.split(DELIMETER)

    if not name in NUMBERS:
      raise Exception(f"Unknown number '{name}'")

    new_name = NUMBERS[name]
    new_content.write(new_name + DELIMETER + num)

with open('new_numbers.txt', 'w') as file:
  file.write(new_content.getvalue())
