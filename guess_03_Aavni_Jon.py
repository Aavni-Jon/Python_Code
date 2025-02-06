#Ch2 - Flow Control - IF/ELIF - Guess-3-Lab
import random

def main():
  # Using an IF/ELSE write a program to have a hard coded variable <user_guess> 
  # compared to a hard coded variable <number_2_guess> and print the results.
  # You will use this source code in the next few program labs
  print('Write a program to compare 2 hard coded numbers with an IF/ELSE')

  # (instructions) Add your code here
  #  1) Add some comments to describe your code guess-03-Aavni-Jon.py
  # -------------------------------------------
  # Add Your Comments Here
  
  # this is my number guessing program
  print('This is a Guessing Game')
  print("Ready to play?")

  # -------------------------------------------

  # (instructions) Add your code here
  #  2) Add some print() statements to describe to the user what is happening and expected.
  print('''A variable that the user is trying to guess and another variable for the user's guess 
  are initialized. This time we take the user's input instead of assigning them an input and 
  randomize the number that the user needs to guess. Then a conditional checks if the user guess 
  is equivalent to the number than needs to be guessed. If it's not the same, then an appropriate 
  message is printed. If it is, then an appropriate message is printed''')

  # (instructions) Add your code here
  #  3) Add a variable: 
  number_2_guess = random.randint(0, 10)

  # (instructions) Add your code here
  # 5) Add a hard coded user guess
  #user_guess = 5
  user_guess = int(input('Enter a number:'))

  # (instructions) Add your code here
  #  6) print the type() of the user_guess to show it is an integer
  #  7) print() the value of the user_guess variable
  print(type(user_guess))
  print(user_guess)

  # (instructions) Add your code here
  #  8) Add an IF statement to check if user_guess is equal to number_2_guess
  #  9) If they are equal, print() something like 'Good Guess, you are a Winner'
  # 10) also print() <user_guess> is equal to <number_2_guess>
  if number_2_guess == user_guess:
    print("Good Guess, you are a Winner")
    print(user_guess, "is equal to", number_2_guess)
  
  # (instructions) Add your code here
  # 11) Add an ELIF statement to check to see if the user_guess is close, 
        #specifically if it's number_2_guess +1 or -1
  # 12) If it is, print out  "Close but no Cigar" and then print the value of user_guess 
        #with the text "is one number away from" and then the number_2_guess 
  elif user_guess + 1 == number_2_guess or user_guess - 1 == number_2_guess:
    print("Close but no Cigar")
    print(user_guess, "is one number away from", number_2_guess)
  
  # (instructions) Add your code here
  # 13) Add an ELSE statement and in that block print() if they are not equal
  # 14) print() something like 'Better Luck Next Time'
  # 15) also print() <user_guess> is NOT equal to <number_2_guess>
  else:
    print("Better luck next time")
    print(user_guess, "is NOT equal to", number_2_guess)

  # (instructions) Add your code here
  # 14) End with a print() that says something like 'All Done!'
  print('All Done!')
  
main()
