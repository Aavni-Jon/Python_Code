#Python Ch1 - Variables, Expressions, Data Types & Operators
#Slideshow: https://docs.google.com/presentation/d/1VsPztt4kfu9cvprFU1RwUPLttx4nOkxAZymEiCSceHU/edit#slide=id.p

def main():
  print("Starting The Code Challenge")
  # Declare Any main() Variables - (Not Global)

  print("Starting <Specific Part> Of Code Challenge")
  # Enter Your Code Here:
  print('Enter Your Code Here:')
  
  x = 42
  print(x)

  #Type
  x = x+5
  print(x)
  type(x)

  #Lab Example #1
  bob = 42
  print(bob)
  type(bob)

  #Lab Example #2
  print(27)
  type(27)

  #Lab Example #3
  my_snake_sound_variable = 'Hissssssss'
  print(my_snake_sound_variable)
  type(my_snake_sound_variable)

  #Lab Example #4
  my_char_variable = '25'
  print(my_char_variable)
  type(my_char_variable)

  #Numeric vs Strings
  #Lab Example #5
  x = 42
  y = 20
  z = x + y
  print(z)
  #space added for visibility
  x = 42
  y = "20"
  z = x + y
  print(z)

  #Floats
  pi = 3.14159265359
  print(pi)
  type(pi)

  #Changing from Integer to Float
  #Lab Example #6
  x = 10
  y = 2
  z = x / y
  print(z)
  #space added for visibility
  y = 3
  z = x / y
  print(z)

  #Integer Divide
  #Lab Example #7
  x = 9
  y = 5
  z = x/y
  print(z)
  type(z)
  
  #Lab Example #8
  z=x//y
  print(z)
  type(z)

  #Order of Operations
  #Lab Example #18
  x = 2*3-1
  print(x)
  #space added for visibility
  x = 6+4/2
  print(x)
  #space added for visibility
  x = 2*(3-1)
  print(x)
  #space added for visibility
  x = (6+4)/2
  print(x)

  #Floats as Scientifics or Engineering Notation
  #Big Numbers
  #Lab Example #9
  x = 2.5e3
  print(x)
  #space added for visibility
  x = 2.5e15
  print(x)
  #space added for visibility
  x = 2.5e16
  print(x)
  
  
  #Small Numbers
  #Lab Example #10
  x = 2.2e-2
  print(x)
  #space added for visibility
  x = 2.2e-4
  print(x)
  #space added for visibility
  x = 2.2e-9
  print(x)

  #Plotting Points/Complex Numbers
  #Lab Example #11
  x = 2.2e-2
  print(x)
  #space added for visibility
  r = x.real
  i = x.imag
  print(r, ",",i)

  #Booleans
  #Lab Example #12
  5 == (3 + 2)
  #space added for visibility
  1 == 2
  #space added for visibility
  "bob" == "Bob"
  #space added for visibility
  x = 9
  6 < x

  #Lab Example #13
  my_bool_var = True
  print(my_bool_var)

  my_bool_var = False
  print(my_bool_var)

  #Assigning a variable
  my_Variable_Name = 99
  my_String = 'Hi there'
  somevariablewithalongname = 5
  x = 10 + somevariablewithalongname
  pi = 3.1415926535897931
  
  #Lab Example #14
  x = 12
  y = 7
  print(x)
  print(y)
  print(x+y)
  
  #Lab Example #15
  x = 9
  print(x)
  print(y)
  print(x+y)

  #Lab Example #16
  x = 14
  print(x)
  x = x+5
  print(x)

  #Simultaneous Assignment
  #Lab Example #17
  x = y = someVar = 42
  print(x, y, someVar)

  

  print("Ending <Specific Part> Of Code Challenge")
  print("Ending The Code Challenge")

main()
