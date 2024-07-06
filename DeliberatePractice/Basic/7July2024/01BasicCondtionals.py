# Set 2: Write if statements with valid syntax
def spaceBar():
  space = ""
  i = 0
  while i < 20:
    space += "%"
    i += 1
  return print(space)

spaceBar()
# 1 Use a variable to store a number, then write a condition that prints 0 if the number is equal to 10, and prints -1 otherwise.
def lessThanTen(num):
  if num < 10:
    return print(0)
  else:
    return print(-1)

lessThanTen(15)
lessThanTen(9)
  

spaceBar()
# 2 Use a variable to store a number, then write a condition that prints -1 if the number is less than 10, prints 1 if the number is greater than 10, and prints 0 if the number is equal to 10.
def aroundNumTen(num):
  if num < 10:
    print(-1)
  elif num == 10:
    print(0)
  else:
    print(1)
aroundNumTen(20)
aroundNumTen(10)
aroundNumTen(9)

spaceBar()

# 3 Use variables to store two numbers, then write a condition that prints 1 if the numbers are both less than 10, and prints 0 otherwise.
def bothNumbers(num1, num2):
  if num1 < 10 and num2 < 10:
    print(1)
  else:
    print(0)

bothNumbers(10, 11)
bothNumbers(9, 10)
bothNumbers(9.9, 9.99)

 # 4 Use a variable to store a number, then write a condition that prints 9 if the number is less than 10, prints 19 if the number is less than 20, prints 29 if the number is less than 30, and prints -1 otherwise (only one print statement should occur).
def lessThanNumbers(num):
  less_than = None 
  if num < 10:
    less_than = 9
  elif num < 20:
    less_than = 19
  elif num < 30:
    less_than = 29
  else:
    less_than = -1
  
  return print(less_than)
lessThanNumbers(20) # 29
lessThanNumbers(40) # -1
lessThanNumbers(9) # 9


 # 5 Use a variable to store a number, then write a condition that prints 1 if the number is over 9000, and prints -1 otherwise

 # 6 Use variables to store two numbers, then write a condition that prints 100 if either number is greater than 10, and prints -100 otherwise.

 # 7 Use a variable to store a number, then write a condition that prints 1776 if the number is less than 0, and prints 1979 otherwise.

 # 8 Use a variable to store a number, then write a condition that prints 100 if the number equals 100, prints 99 if the number is equal to 99, and prints 0 otherwise.

 # 9 Use variables to store two numbers, then write a condition that prints 1 if the first number is less than zero and the second number is greater than 0, and prints 0 otherwise.

 # 10 Use a variable to store a number, then write a condition that prints 5 if the number is greater than 80, prints 4 if the number is greater than 60, prints 3 if the number is greater than 40, prints 2 if the number is greater than 20, and prints 1 otherwise (only one print statement should occur).