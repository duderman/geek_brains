def append_info(info, name, val):
  """
  Appends named value if it's present
  """
  if val is None:
    return

  info.append(f"{name}: {val}")


def print_info(first_name=None, last_name=None, dob=None, city=None, email=None, phone=None):
  """
  Prints info about a user
  """
  info = []
  append_info(info, 'First name', first_name)
  append_info(info, 'Last name', last_name)
  append_info(info, 'DOB', dob)
  append_info(info, 'City', city)
  append_info(info, 'Email', email)
  append_info(info, 'Phone number', phone)

  print(', '.join(info))


print_info(first_name='Kolka', last_name='Bog', city='London')
