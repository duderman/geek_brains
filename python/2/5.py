list = [7, 5, 3, 3, 2]

while True:
  try:
    user_input = input("num: ")
    if user_input == '':
      break
    n = int(user_input)
    list.append(n)
    list.sort()
    list.reverse()
    print(list)
  except ValueError:
    print("Not a number")
