#Ch2 - Flow Control - IF/ELIF - Guess-2-Lab

def main():
  # Using an IF/ELSE write a program to have a hard coded variable <user_guess> 
  # compared to a hard coded variable <number_2_guess> and print the results.
  # You will use this source code in the next few program labs
  print('Write a program to compare 2 hard coded numbers with an IF/ELSE')

  # (instructions) Add your code here
  #  1) Add some comments to describe your code guess-02-Aavni-Jon.py
  # -------------------------------------------
  # Add Your Comments Here
  
  # this is my number guessing program
  print('This is a Guessing Game')
  print("Ready to play?")

  # -------------------------------------------

  # (instructions) Add your code here
  #  2) Add some print() statements to describe to the user what is happening and expected.
  print('''A variable that the user is trying to guess and another variable for the user's guess 
  are initialized. This time we take the user's input instead of assigning them an input.
  Then a conditional checks if the user guess is equivalent to the number than needs to be guessed. 
  If it's not the same, then an appropriate message is printed. If it is, then an appropriate 
  message is printed''')

  # (instructions) Add your code here
  #  3) Add a variable: 
  number_2_guess = 7
  
  #  4) print() the variable number_2_guess
  print(number_2_guess)

  # (instructions) Add your code here
  # 5) Add a hard coded user guess
  user_guess = input('Enter a number:')

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
  # 11) Add an ELSE statement and in that block print() if they are not equal
  # 12) print() something like 'Better Luck Next Time'
  # 13) also print() <user_guess> is NOT equal to <number_2_guess>
  else:
    print("Better luck next time")
    print(user_guess, "is NOT equal to", number_2_guess)

  # (instructions) Add your code here
  # 14) End with a print() that says something like 'All Done!'
  print('All Done!')
  
main()
