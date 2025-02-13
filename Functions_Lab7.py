#Ch 3 - Functions - Lab #7 - User Functions - my_math2()

# Functions - Passing Arguments
print('''Functions - Passing Arguments''')      
print('''Challenge #4
Run this code, then edit
Create a single function that takes the 2 argument numbers x,y 
and a 3rd argument, that selects between Addition, Subtraction, 
Multiplication, and Division, with the default being Addition. 
Then returns the result

Print the math operation and then the resulting equation

Enter Code Here:
----------------------------------------------------      ''')
# Edit and Enter Code Here:
def math(x,y,z) :
  if z == "subtract":
    r = x - y
  elif z == "multiply":
    r = x*y
  elif z == "divide":
    r = x/y
  else:
    r = x + y
  return r

def main():
  my_num_1 = input("Enter an integer:") #5
  my_num_2 = input("Enter another integer:") #2
 
  x = True
  while x :
    try :
      my_num_1 = int(my_num_1)
      my_num_2 = int(my_num_2)
      x = False
    except :
      print("One or both is not an integer")
      my_num_1 = input("Enter an integer:")
      my_num_2 = input("Enter another integer:")
 
  else :
    print("Enter in lower case")
    choice = input("Do you want to add, subtract, multiply, or divide?:")
    solution = math(my_num_1, my_num_2, choice)
    if choice == "subtract":
      print("You chose to subtract")
      print(my_num_1, "-", my_num_2, "=", solution)
    elif choice == "multiply":
      print("You chose to multiply")
      print(my_num_1, "x", my_num_2, "=", solution)
    elif choice == "divide":
      print("You chose to divide")
      print(my_num_1, "/", my_num_2, "=", solution)
    else:
      print("You chose to add")
      print(my_num_1, "+", my_num_2, "=", solution)

main()
print('Done with Challenge 4')

print('''----------------------------------------------------''')

print('''Challenge #5
in the main() function, add an input() request to get the x,y values.
- make sure they are numbers.
- in a while loop keep asking for the 2 values if one or both are 
  not a number
- make sure you do valid Error and Exception testing.
    ''')
