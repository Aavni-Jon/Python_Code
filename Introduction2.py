#Ch 2 - Flow Control - IF/ELSE

def main():
  print(7 == 7)
  print(9 == 7)

  print(type(5))
  print(type(9 == 7))
  print(type(True))
  print(type(False))

  #Lab Example #1 - If Statement
  x = 12
  if x > 9:
    print("The if statement was evaluated as True")

  #Lab Example #2 - If Statement
  x = 12
  if x > 9: 
    print("x is equal to or greater than 9")

  #Lab Example #3 - If Statement and Some Formating of the Output
  x = 12
  y = 8
  if x >= y: 
    print(x, " is equal to or greater than ", y)

  #Lab Example #4 - If Statement and Some Formating of the Output
  x = input("Enter a number > ")
  # Convert a type 'str' to type 'int'
  x = int(x) 
  y = 8
  if x >= y :
    print(x, "is equal to or greater than", y)
  print('Done')

  #Lab Example #5 - If/else Statement and Some Formating of the Output
  x = input("Enter a number > ")
  # Adding to convert a type 'str' to type 'int'
  x = int(x) 
  y = 8
  if x >= y :
    print(x, "is equal to or greater than", y)
  else:
    print(x, "is less than", y)
  print('Done')

  #Lab Example #6 - If/else Statement and Some Formating of the Output
  x = input("Enter a number > ")
  # Convert a type 'str' to type 'int'
  x = int(x) 
  y = 8
  if x > y :
    print(x, "is greater than", y)
  elif x == y:
    print(x, "is equal to ", y)
  else:
    print(x, "is less than ", y)
  print('Done')

main()
