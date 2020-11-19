DEFAULT_ERROR_MESSAGE = 'Wrong number'


def ask_int(what, check=None, msg=None):
  if msg is None:
    msg = DEFAULT_ERROR_MESSAGE
  while True:
    try:
      n = int(input(f"{what}: "))
      if __perform_check(n, check, msg):
        return n
    except ValueError:
      print("Not a number")


def __perform_check(n, check, msg):
  if check is None:
    return True
  else:
    if check(n):
      return True
    else:
      print(msg)
      return False
