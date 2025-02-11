#Ch 3 - Functions - Lab #2 - min() & max() Functions
# Functions Introduction

# Python Lab - Functions - min() max()
def main():
  print('Playing with Builtin Python Functions')
  print('min() max()')
  student_name = "Aavni Jon"
  program_creation_date = "02/11/2025"
  print(student_name)
  print(program_creation_date)
  print('''Functions Introduction''') 
  print('''This Lab is about using Python Builtin Functions min() and max().
  Try and show code using the following functions:
  - max()
  - min()
  
  My code follows:''')
  print(''' Challenge #1
  Run, then make sure you understand why is "s" bigger than "S" and why a blank space is printed:
        
  Using the built-in Functions max() & min()
  - Why is "s" bigger than "S"? : It comes after it in the ascii table
  - Why does it look like the "smallest" did not print anything? : Its a space
  - Is it what you expected? Can you explain it? : Yes, the space comes before 'A' in the ascii table
  Check out the link to the Extended ASCII Table Codes https://www.ascii-code.com/  ''')
  
  my_string = 'STEAM Is Cool'
  print('The variable "my_string" = ', my_string)
  biggest = max(my_string)
  print('The biggest character in the \nstring "STEAM Is Cool" is', biggest)
  smallest = min(my_string)
  print('The smallest character in the \nstring "STEAM Is Cool" is', smallest)
  print('Done with Challenge 1')
  
  print('''Challenge #2
  Update the code above to use the input() function and ask the user for a long sentence string 
  and assign it to the variable 'my_string'
  
  With this new user input string, see what the min() and  max() character is. ''')      

  my_string = str(input("Enter a long sentence string: "))
  print('The variable "my_string" = ', my_string)
  biggest = max(my_string)
  print('The biggest character in the \nstring', my_string, 'is', biggest)
  smallest = min(my_string)
  print('The smallest character in the \nstring', my_string, 'is' ,smallest)
  print('Done with Challenge 2')
  
main()
