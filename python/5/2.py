lines = []

try:
  with open('echo.txt') as file:
    for line in file:
      line_length = len(line.strip())
      lines.append(line_length)
  msgs = [f"line {i+1} has {lines[i]} chars" for i in range(len(lines))]
  chars_msg = ', '.join(msgs).capitalize()

  print(f"{chars_msg}. Lines count: {len(lines)}")
except FileNotFoundError:
  print('No such file')
except IOError:
  print('Something went wrong')
