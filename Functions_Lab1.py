#Ch 3 - Functions - Lab #1 - Built-In Functions

def main():
  # Python Lab
  print('Playing with Builtin Python Functions')
  student_name = "Aavni Jon"
  program_creation_date = "02/10/2025"
  print(student_name)
  print(program_creation_date)
  print('''Functions Introduction
  There is a big list of built-in functions here:
  https://www.w3schools.com/python/python_ref_functions.asp
  ''')     
  print('''This Lab is about using Python Builtin Functions. Try and show code using the following functions, then pick 4 more to try. ...
  - print()
  - input('enter something here: ')
  - int()
  - type()
  - abs()
  - len()
  
  My code follows:''')
  # update the 'student_name' and 'program_creation_date' variables and add your code here:
  #print()
  print("Hello, world!")
  #input()
  name = input("What is your name? ")
  print("Hello, " + name)
  #int()
  number = "42"
  integer = int(number)
  print(integer)
  #type()
  x = 'c'
  print(type(x))
  #abs()
  x = abs(-20)
  print(x)
  #len()
  x = []
  print(len(x))
  #hex()
  x = hex(255)
  print(x)
  #bin()
  x = bin(36)
  print(x)
  #ascii()
  x = ascii("åéïœū")
  print(x)
  #pow
  x = pow(2, 3)
  print(x)

  main()
