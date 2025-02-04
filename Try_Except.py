#Ch 2 - Flow Control - TRY & EXCEPT

def main():
  print("Starting The Code Challenge")
  # Declare Any main() Variables - (Not Global)

  print("Starting <Specific Part> Of Code Challenge")
  # Enter Your Code Here:
  print('Enter Your Code Here:')
  x = 42
  print(x)

  #Lab Example # 1 - Syntax Error
  x = 7
  print(x)) #syntax error ')'

  #Lab Example # 2 - Syntax Error
  x = 7
  print(x)
  if x = 7 : #syntax error '=' instead of '=='
    print(x,"is equal to Seven")

  #Lab Example # 3 - Traceback Error
  x = input("enter a number > ")
  #add next line to avoid error
  x = int(x)  # this converts the input string to an integer
  print(x)
  print(type(x))
  y = x + 5 #TypeError: must be str, not int
  print(y)

  #Lab Example # 4 - Traceback Error
  my_number = input("enter a number > ") #add the literal 'FUN' causes...
  my_number = int(my_number) #ValueError: invalid literal for int() with base 10: 'FUN'
  print(my_number, 'is a number')

  print('done')
  
  #Lab Example # 5 - "trapping" a non-numeric value with the "TRY"
  my_number = input("enter a number > ")
  try:
    my_number = int(my_number)
    print(my_number, 'is a number')
  except: 
    print('Please enter a number')
    print(my_number, 'is NOT a number')
  print('done')

  print("Ending <Specific Part> Of Code Challenge")
  print("Ending The Code Challenge")

main()
