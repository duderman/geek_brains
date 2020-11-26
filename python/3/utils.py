DEFAULT_ERROR_MESSAGE = 'Wrong number'


def ask_int(what, check=None, msg=DEFAULT_ERROR_MESSAGE):
  """Asks user for an int

  Args:
      what (string): Prompt text
      check (lambda, optional): Func with an additional int check. Must return bool
      msg (string, optional): [description]. Defaults to 'Wrong number'.

  Returns:
      int: User input as int
  """
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
