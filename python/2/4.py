MAX_WORD_LENGTH = 10

list = input('wut: ').split()

for i in range(len(list)):
  word = list[i]
  if len(word) > MAX_WORD_LENGTH:
    word = word[0:MAX_WORD_LENGTH] + '...'
  print('{}: {}'.format(i, word))
