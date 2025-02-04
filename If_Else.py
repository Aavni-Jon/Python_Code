#Ch 2 - W3-Schools Review - Flow Control - If/Else
#https://www.w3schools.com/python/python_conditions.asp

def main():
  print("Starting The Code Challenge")
  # Declare Any main() Variables - (Not Global)

  print("Starting <Specific Part> Of Code Challenge")
  # Enter Your Code Here:
  print('Enter Your Code Here:')
  x = 42
  print(x)

  #Basic syntax
  a = 33
  b = 200
  if b > a:
    print("b is greater than a") #raise error if not indented

  #Elif
  a = 33
  b = 33
  if b > a:
    print("b is greater than a")
  elif a == b:
    print("a and b are equal")

  #Else
  a = 200
  b = 33
  if b > a:
    print("b is greater than a")
  elif a == b:
    print("a and b are equal")
  else:
    print("a is greater than b")

  #Else w/o Elif
  a = 200
  b = 33
  if b > a:
    print("b is greater than a")
  else:
    print("b is not greater than a")

  #Short hand if -- Only one statement to execute
  if a > b: print("a is greater than b")

  #Short hand If Else - Only one stateent for if and only one for else
  a = 2
  b = 330
  print("A") if a > b else print("B")

  #Multiple if else statements on one line
  a = 330
  b = 330
  print("A") if a > b else print("=") if a == b else print("B")

  #'and' keyword
  a = 200
  b = 33
  c = 500
  if a > b and c > a:
    print("Both conditions are True")

  #'or' keyword
  a = 200
  b = 33
  c = 500
  if a > b or a > c:
    print("At least one of the conditions is True")

  #'not' keyword
  a = 33
  b = 200
  if not a > b:
    print("a is NOT greater than b")

  #Nested If
  x = 41
  if x > 10:
    print("Above ten,")
    if x > 20:
      print("and also above 20!")
    else:
      print("but not above 20.")

  #The 'pass' Statement -- if you have an empty if statement, then put in 'pass' to avoid error
  a = 33
  b = 200
  if b > a:
    pass

  print("Ending <Specific Part> Of Code Challenge")
  print("Ending The Code Challenge")

main()
