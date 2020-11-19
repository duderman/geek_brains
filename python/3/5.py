nums = []

while True:
  try:
    data = input("Input: ")
    for n in data.split():
      nums.append(int(n))
  except ValueError:
    break
  finally:
    result = sum(nums)
    print(f"Sum: {result}")
