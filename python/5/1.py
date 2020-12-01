with open('echo.txt', 'w') as file:
  while True:
    text = input('sup?: ')
    if text == '':
      break
    file.write(text + "\n")
