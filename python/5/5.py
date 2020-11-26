from random import randrange

nums = []
for i in range(10):
  num = randrange(100)
  num_s = str(num)
  nums.append(num_s)

with open('randoms.txt', 'w') as file:
  content = ' '.join(nums)
  file.write(content)

with open('randoms.txt') as file:
  nums = file.readline().split()
  nums = map(lambda num: int(num), nums)

sum = sum(nums)
print(f"Sum: {sum}")
