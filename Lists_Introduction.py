#Ch 4 - Lists - Lab #1 - List Introduction

def main():

  # Python LIST Lab1
  print('''Python Lists - Introduction 
  Lists are comma delimited groups of variables

  Challenge #1
  Run the code, make sure you understand how the list is constructed
      
  - Can you explain the difference between a single object 
    variable and a list?
    : Single is only one object, list can have multiple objects
  - Can you explain how lists are comma delimited sets of objects?
    : Each object is separeted by a comma''') 

  # x = a single object
  print('''x = 9, x is a single variable object''')
  x = 9
  print(x)
  print(type(x))

  # x = a list of objects
  x = [1, 2, 5, 66, 42, 19]
  print('\nx = ',x,'x is now a list of objects')
  print(x)
  print(type(x))

# x = a list of mixed Type objects
  x = ['fName', 'lName', 25, True, 4.2]
  print('\nx = ',x,'x is now a list of mixed objects')
  print(x)
  print(type(x))

# Challenge 2
  print('''Challenge #2 
  - Create a new list of integers
  - Create a new list of character strings
  - Create a new list of mixed integers, floats, and strings

  Enter your code here:
  ------------------------------------''')
# Enter your code here:
  print('------------------------------------')
  intList = [1, 2, 5, 66, 42, 19]
  charlist = ['a', 'b', 'c', 'd', 'e', 'f']
  mixList = [1, 'a', 2.0, "Hello", 3, 'b', "4.0"]

main()
