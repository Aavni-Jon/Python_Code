#Ch 1 - W3-Schools Review - Variables Assign Multiple Values

def main():
#Assign multiple variables in one line
  x, y, z = "Orange", "Banana", "Cherry"
  print(x)
  print(y)
  print(z)

#Assign same value to multiple variables in one line
 x = y = z = "Orange"
 print(x)
 print(y)
 print(z)

#Unpacking (extract values into variables)
 fruits = ["apple", "banana", "cherry"]
 x, y, z = fruits
 print(x)
 print(y)
 print(z)

main()
