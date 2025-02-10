# Python WHILE - Do Math On User Input Lab - Scratch Pad

'''
Coding Challenge:
WHILE - Do Math On User Input Lab 

Use the following Pseudocode to wrtie a program:

 - Ask user for an integer number greater than 20
 - Don't forget test the <user_number> to see if it's an integer
 - Set our initial <count> variable to 0
 - While our <User_number> is greater than 1
 - Divide the <user_number> by 2
 - Increase our <count> by 1
 - end

Expected Output: If the user_number was 20:

  Starting Code Challenge
  Enter an integer number 20 or greater >20
  Your number 20 is a valid Integer 20 or greater.  Thanks
  Starting While Loop - Print Count Variable
  The user input started as  20
  The current value of the user input after some math is 10.0
  The while loop has looped 1 time
  The current value of the user input after some math is 5.0
  The while loop has looped 2 time
  The current value of the user input after some math is 2.5
  The while loop has looped 3 time
  The current value of the user input after some math is 1.25
  The while loop has looped 4 time
  The current value of the user input after some math is 0.625
  The while loop has looped 5 time
  Ending While Loop
  The While Loop, looped a total of 5 times
  Ending Code Challenge
'''
# Your Code Starts Here:
def main():
  print("Starting Code Challenge")
  
  # Declare Any main() Variables - (Not Global)
  user_input = int(input("Enter an integer number 20 or greater > 20: "))
  print("Your number", user_input, "is a valid Integer 20 or greater.  Thanks")
  print("Starting While Loop - Print Count Variable")
  
  # Enter Your Code Here:
  print("The user input started as", user_input)
  count = 0
  while user_input > 1:
      user_input = float(user_input) / 2
      count+=1
      print("The current value of the user input after some math is", user_input)
      print("The while loop has looped", count, "time")

  print("Ending While Loop")
  print("The While Loop, looped a total of", count, "times")
  print("Ending Code Challenge")

main()
