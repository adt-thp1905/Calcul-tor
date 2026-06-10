x = float(input("Enter number 1 :"))
y = float(input("Enter number 2 :"))
z = input("Enter the desired operation: ")
if z == "+"
  print(x + y)
elif z == "-"
  print(x - y)
elif z == "*"
  print(x * y)
elif z == "/"
  if y != 0
   print(x/y)
  else
   print("Cannot divide by zero")
else 
  print("Invalid operator")
