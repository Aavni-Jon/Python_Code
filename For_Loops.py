#Ch 2 - Flow Control - FOR Loop
#https://www.w3schools.com/python/python_for_loops.asp

def main():
  fruits = ["apple", "banana", "cherry"]
  for x in fruits:
    print(x)

  #Looping through a String
  for x in "banana":
    print(x)

  #The break Statement
  #exit loop when x is banana
  for x in fruits:
    print(x)
    if x == "banana":
      break
  #same thing but break comes before print
  fruits = ["apple", "banana", "cherry"]
    for x in fruits:
    if x == "banana":
      break
    print(x)

  #The continue Statement
  fruits = ["apple", "banana", "cherry"]
  for x in fruits:
    if x == "banana":
      continue
    print(x)

  #The range() Function
  for x in range(6): # Values from 0 to 5, NOT 0 to 6
    print(x)
  #Start parameter is 2
  for x in range(2, 6):
    print(x)
  #Increment the sequence with 3 (default is 1):
  for x in range(2, 30, 3):
    print(x)
    
  #Else in For Loop
  #Print all numbers from 0 to 5, and print a message when the loop has ended:
  for x in range(6):
    print(x)
  else:
    print("Finally finished!")
  #fhe else block will NOT be executed if the loop is stopped by a break statement.
  for x in range(6):
    if x == 3: break
    print(x)
  else:
    print("Finally finished!")

  #Nested Loops
  #The "inner loop" will be executed one time for each iteration of the "outer loop":
  adj = ["red", "big", "tasty"]
  fruits = ["apple", "banana", "cherry"]
  for x in adj:
    for y in fruits:
      print(x, y)

  #The pass Statement - avoid error for empty for loops
  for x in [0, 1, 2]:
    pass
  
main()
