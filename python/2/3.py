import sys

months_list = ['winter'] * 2 + ['spring'] * \
    3 + ['summer'] * 3 + ['autumn'] * 3 + ['winter']

months_dict = {}

for i in range(len(months_list)):
  months_dict[i + 1] = months_list[i]

try:
  n = int(input("Month num: "))
  if n < 1 or n > 12:
    print("Wrong number. It should be within 1..12 range")
    sys.exit(1)
except ValueError:
  print("Not a number")
  sys.exit(1)

print(months_list[n - 1])
print(months_dict[n])
