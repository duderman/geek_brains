def int_func(word):
  """
  Makes first letter capital
  """
  return word[0].upper() + word[1:len(word)]


text = input('Text: ')
words = map(int_func, text.split())
result = ' '.join(words)

print(f"Result: {result}")
