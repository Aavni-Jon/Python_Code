#Ch2 - Flow Control - guess-3.py

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
  are initialized. This time we take the user's input instead of assigning them an input. We are 
  also using Try/Except for the integer conversion. Then a conditional checks if the user guess 
  is equivalent to the number than needs to be guessed. If it's not the same, then an appropriate 
  message is printed. If it is, then an appropriate message is printed''')

  number_2_guess = 7
  print(number_2_guess)

  user_guess = input('Enter a number from 0 to 10:')
  ## (instructions) for TRY/EXCEPT
  # 1) make the user_guess = int(user_guess) the test in the TRY statement 
  # 2) have the EXCEPT block print something like 
  #    print "<user_guess> is not a number. Next time enter a number"
  # 3) have all your output code be in the ELSE block of the TRY structure
  try :
    user_guess = int(user_guess)
  except:
    print(user_guess, "is not a number. Next time enter a number.")
  else:
    if number_2_guess == user_guess:
      print("Good Guess, you are a Winner")
      print(user_guess, "is equal to", number_2_guess)
    elif user_guess + 1 == number_2_guess or user_guess - 1 == number_2_guess:
      print("Close but no Cigar")
      print(user_guess, "is one number away from", number_2_guess)
    else:
      print("Better luck next time")
      print(user_guess, "is NOT equal to", number_2_guess)
    print('All Done!')
  
main()
