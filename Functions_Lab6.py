#Ch 3 - Functions - Lab #6 - User Functions - my_math()

# Functions - Passing Arguments
print('''Functions - Passing Arguments''')      
print('''Challenge #1
Run, then Edit the code in the template example:
      
Can you follow and explain
- How arguments are passed from the main code to the function? : Through parameters
- Can you explain how a value is 'returned' : 'return' statement returns value to where 
  the function was called ''')
print('''----------------------------------------------------''')

def my_math(x,y) :
  z=x+y
  return z

def main():
  my_num_1 = 5
  my_num_2 = 2
  sum = my_math(my_num_1, my_num_2)
  print("The sum of", my_num_1, "+", my_num_2, "=",sum)

main()
print('Done with Challenge 1')
print('''----------------------------------------------------''')

print('''Challenge #2
Create a function that multiplies 2 numbers and returns the result
Enter Code Here:
----------------------------------------------------      ''')
# Enter Code Here:
def multiply(x,y) :
  z = x * y
  return z

def main():
  my_num_1 = 5
  my_num_2 = 2
  product = multiply(my_num_1, my_num_2)
  print("The product of", my_num_1, "x", my_num_2, "=", product)

print('''
----------------------------------------------------
''')

print('''
Challenge #3
Create a function that adds 2 numbers and if the result is odd, adds 1, then returns the result
Enter Code Here:
----------------------------------------------------      ''')
# Enter Code Here:
def add(x,y) :
  z = x + y
  if z % 2 != 0:
    z+= 1
  return z

def main():
  my_num_1 = 5
  my_num_2 = 2
  sum = add(my_num_1, my_num_2)
  print("The even number sum of", my_num_1, "+", my_num_2, "=", sum)
print('''----------------------------------------------------''')

print('''Challenge #4
Create a single function that takes the 2 argument numbers x,y 
and a 3rd argument, that selects between Addition, Subtraction, 
Multiplication, and Division, with the default being Addition. 
Then returns the result
Enter Code Here:
----------------------------------------------------      ''')
# Enter Code Here:
def math(x,y,z) :
  if z == "subtraction":
    r = x - y
  elif z == "multiply":
    r = x*y
  elif z == "divide":
    r = x/y
  else:
    r = x+y
  return r

def main():
  my_num_1 = 5
  my_num_2 = 2
  print("Enter in lower case")
  choice = input("Do you want to add, subtract, multiply, or divide?:")
  solution = math(my_num_1, my_num_2, choice)
  print("The first number is", my_num_1, "and the second number is", my_num_2, 
        "\nYour solution is", solution)
print('''----------------------------------------------------''')
