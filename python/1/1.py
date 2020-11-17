a = ""
b = 1

str_input = input("SUP?: ")
print("str_input is: ", str_input)

try:
  int_input = int(input("SUP(int)?: "))
except ValueError:
  print("Not a number")
else:
  print("int_input is :", int_input)
