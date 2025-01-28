#8.1.2.2.1 - Chapter 2  - Python - Flow Control - IF/ELIF/ELSE - STEAM Clown
#Labs from: https://docs.google.com/presentation/d/1nMybtjErJBdFNQ6iDcKxfz-XPAiZnrEsZGtcSN_qJwA/edit#slide=id.gc91dee5b12_0_175 

# Python Lab 1 - Asking Questions - Introduction
# Replit: https://replit.com/@STEAMClown/Py-Ch2-Lab1-Asking-Questions-Intro#main.py
print('''
Challenge #1
----------------------------------------------------
Can you explain?

What do the following mean?
1) Assignment: Assign values to variables using an assignmnt operator.
2) Comparison: Ask a question using a comparison operator. If they are equal it will return True, False if they aren't.
3) Evaluation: Follows operator precedence to do the intended task, such as printing the intended result. 
4) What is the difference between "=" and "==": "=" is an assignment operator, "==" is a comparison operator.
5) Boolean: True or False value after performin a comparison or evaluation.
      
Hint: https://www.w3schools.com/python/python_operators.asp
---
''')

# Comparing Variables and Objects - Lab 2
# Challenge - Compare Variables or Objects For Equivalence: 
print('''
Challenge #1
----------------------------------------------------
Try changing the values of x and y and see what happends
      
Hint: https://www.w3schools.com/python/python_operators.asp
----------------------------------------------------
''')
print('''Answer to Challenge 1
-------------------------------------------------''')
x=9 #10
y=15 #9
print("x = ", x)
print("y = ", y)
print("x == y \t\tis ", x == y)
print("x != y \t\tis ", x != y)
print("x > y \t\tis ", x > y)
print("x < y \t\tis ", x < y)
print("x >= y \t\tis ", x >= y)
print("x <= y \t\tis ", x <= y)
print("x is y \t\tis ", x is y)
print("x is not y \tis ", x is not y)
print('''-------------------------------------------------''')


# Asking a Question with 'IF' - Lab 3
# Challenge 1 - Write and play with "IF"
print('''
Challenge # 1
----------------------------------------------------
Run this code, review it, and then change the comparison operation.
      
Ways to compare objects
      
x == y      # x is equal to y
x != y      # x is not equal to y
x > y       # x is greater than y
x < y       # x is less than y
x >= y      # x is greater than or equal to y
x <= y      # x is less than or equal to y
x is y      # x is the same as y
x is not y  # x is not the same as y      

# If you change the comparison operation, remember to change 
it in the print statement too
---
''')
# -------------------------------------------------
print('''Answer to Challenge 1
-------------------------------------------------''')
x = 5
y = 9
z = 12
print("x =",x)
print("y =",y)
print("z =",z)
if x < y : 
  print("The if statement",x,"<",y,"was evaluated as 'True'")

if x > z : 
  print("The if statement",x,">",z,"was evaluated as 'True'")

if x == z : 
  print("The if statement",x,"==",z,"was evaluated as 'True'")

if x == y-4 : 
  print("The if statement",x,"==",y-4,"was evaluated as 'True'")
print('''
Add 3-4 more of your own if statements
-------------------------------------------------''')
if x != y : 
  print("The if statement",x,"!=",y,"was evaluated as 'True'")

if x >= y-4 : 
  print("The if statement",x,">=",y-4,"was evaluated as 'True'")

if z <= y+3 : 
  print("The if statement",z,"<=",y+3,"was evaluated as 'True'")
  

# Comparing User Input - Lab 4
# More IF statements
print(''' Challenge # 1
----------------------------------------------------
Try entering different numbers and make sure you understand why each
'IF' statement was run.  The 'print()' in each "IF" statement will run 
only if it is 'True'. 

You will compare User input "x" to the variable "y"
Is the Answer "TRUE"?
      
Hint: Check out W3Schools IF
- https://www.w3schools.com/python/python_conditions.asp
----------------------------------------------------
''')
x = input("Enter a number > ")
# All User input is type 'str'
print("The User input the value ",x)
print("The type of input",x,"is",type(x))
# Convert a type 'str' to type 'int'
x = int(x) 
print("After using the function int(x), the type of input",x,"is",type(x),"\n")
y = 8
print('x =',x)
print('y =',y)
print("You will now compare the User input",x,"with the value of y which is",y)
if x == y :
  print(x, "is equal to ", y)

if x >= y :
  print(x, "is > than or equal to", y)

if x <= y :
  print(x, "is < than or equal to", y)

if x > y :
  print(x, "is > than", y)

if x < y :
  print(x, "is < than", y)

if x != y :
  print(x, "is not equal to", y)

if x is y :
  print(x, "is the same as", y)

if x is not y :
  print(x, "is not the same as", y)

print('\nDone')


# Two Questions / Three Choices - Lab 5
# IF ELIF ELSE statements
print('''Asking Questions and having 2-3 different program control paths:

This Lab is about Asking Questions and being able to make 
2-3 different program control decisions  
      
1) IF lets you ask 1 question

2) IF/ELSE lets you ask 1 question, but make 2 decisions based 
on the answer.

3) IF/ELIF/ELSE lets you ask 1 question with 2 choices, and 
based on the answer, you can ask another question with 2 
more choices. 

With an IF/ELIF/ELSE, you will always have at least 1 of 3 
program control choices. 

Challenge # 1
----------------------------------------------------
Explore how an IF/ELIF/ELSE works and  make sure you understand 
why each IF/ELIF/ELSE was true, and why one of the 3 statements 
were run.  
      
The statements indented under and IF/ELIF/ELSE only run 
if that statement was 'True', or is the default ELSE option. 
      
Hint: Check out W3Schools IF
- https://www.w3schools.com/python/python_conditions.asp
----------------------------------------------------
''')
x = input("Enter a number > ")
# Convert a type 'str' to type 'int'
x = int(x)
y = 8

if x == y :
  print(x, "is equal to", y)
elif x > y:
  print(x, "is greater than", y)
else :
  print(x, "is less than", y)

print('Done')


# Guess A Random Number - Lab 6
print('''Asking Questions - Guess if a random number =, is over, or under.

You will write a program that will use the random() function, 
to store a random number from 0-5  You will then ask the 
User to see if they can guess the random number.  Ask the 
User to input a number, compare that number with the 
random number, and print out if they guessed it, or if 
their guess is above or below.
      ''')

print('''
Challenge # 1
----------------------------------------------------
Start writing your code:

Where should you start? Break it down!!!
      
1) random() - Learn about the random function.  Create a 
  variable, like computer_random, and assign it a random number, 
  then print(computer_random)
      
2) Get the guess from the User and assign it to a variable, 
   like user_guess, and print(user_guess)


3) Using an IF/ELIF/ELSE Test to see if the variable 
   computer_random = user_guess
  - If they are equal, print some message, like "WooHoooo, they are equal"
  - If they are not equal, use the elif to test if the guess 
    is less than the random number, and print an appropriate message.
  - If that is not 'True' then then number must be bigger, so 
    in the else, print an appropriate message.

Hint:
https://www.w3schools.com/python/ref_random_randint.asp
https://www.w3schools.com/python/python_operators.asp
---
''')
# -------------------------------------------------
print('''Answer to Challenge 1
-------------------------------------------------''')
# Type your code and comments here:
import random

computer_random = random().randint(0, 5) #inclusive

user_guess = input("Guess a random number between 0 and 5")
user_guess = int(user_guess)

if user_guess == computer_random:
  print("WooHoooo, they are equal")
elif user_guess < computer_random:
  print(user_guess, "is less than the random number")
else :
  print(user_guess, "is greater than the random number")

print('''
-------------------------------------------------''')




