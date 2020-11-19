def ask_int(what):
  while True:
    try:
      return int(input(f"{what}: "))
    except ValueError:
      print("Not a number")
