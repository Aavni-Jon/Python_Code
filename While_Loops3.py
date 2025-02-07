#Ch2 - Flow Control -WHILE - Compare User Input To Count Variable

# Python WHILE Loop - Compare User Input To Count Variable Lab
# Use this Replit to try some code... Use it as a scratch pad.

'''
Coding Challenge:
WHILE Loop - Compare User Input To Count Variable Lab

This Challenge is to write code that: 
Asks the user for an integer number 0 to 9 as input
Validate it's an integer (Hint: use your TRY/EXCEPT code)
Prints out the user input.  
Then use a while loop with a count variable, and loop from 0 to 10, and check when the user input variable matches the count variable.
When the user variable and the count variable are equal, print "The User variable is equal to the count variable. User = <the user variable value> Count variable = <the count variable>" 
  
Expected Output: If the user variable input was "6"
    Starting Code Challenge
6
Starting While Loop - Comparing User & Count Variable
0
1
2
3
4
5
The User variable is equal to the count variable. 
User = 6 
Count = 6
7
8
9
Starting While Loop
End Code Challenge

'''

# Your Code Starts Here:
# Enter Your Code Here:

def main():
  print("Starting Code Challenge")
  # Print The User Input
  print("Starting While Loop - Print Count Variable")
    
  user_input = input("Enter an integer from 0-9 : ")
  print("The number is", user_input)

  x = True
  while x :
    try :
      user_input = int(user_input)
      x = False
    except :
      print(user_input, "is not an integer.")
      user_input = input("Enter an integer from 0-9 : ")
  else :
    count = 0
    while count < 10:
      if count == user_input:
        print("The User variable is equal to the count variable.")
        print("User =", user_input)
        print("Count variable =", count)
      print(count)
      count+=1
        
  print("Ending While Loop")
  print("Ending Code Challenge")

main()
