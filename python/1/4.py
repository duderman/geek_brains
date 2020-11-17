try:
  n = input("n: ")

  max = 0
  i = 0

  while i < len(n):
    curr = int(n[i])
    if curr > max:
      max = curr
    i += 1
except ValueError:
  print("Not a number")
  exit(1)

print("max: ", max)
