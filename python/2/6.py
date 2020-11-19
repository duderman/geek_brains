items = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

data = {}


def add_data(data, info):
  for item in info.items():
    if item[0] not in data:
      data[item[0]] = set([])
    data[item[0]].add(item[1])


for item in items:
  add_data(data, item[1])

print(data)
