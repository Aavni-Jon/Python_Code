# Python While Loop - Incrementing a Count Variable Lab - Scratch Pad

'''
Coding Challenge:
While Loop - Print A Count Value - This Challenge is to write 
code that uses a while loop to print the value of a counter 
variable that starts at 0 and loops up to 10.  It should 
print 0-9 and then on the tenth test quit out of the loop.

Expected Output:

  Starting While Loop - Print Count Variable
  0
  1
  2
  …
  8
  9
  Ending While Loop
'''
# Add a Comment Here to describe/explain what you are doing

# Code Started Here:
def main():
  print("Starting While Loop - Print Count Variable")
  # Enter Your Code Here:
  counter = 0
  while counter < 10:
    print(counter)
    counter+=1
  
  print("Ending While Loop")

main()
