#Ch 2 - W3-Schools Review - Flow Control - TRY/EXCEPT
#https://www.w3schools.com/python/python_try_except.asp

def main():
  print("Starting The Code Challenge")
  # Declare Any main() Variables - (Not Global)

  print("Starting <Specific Part> Of Code Challenge")
  # Enter Your Code Here:
  print('Enter Your Code Here:')

  #Exception Handling
  try:
    print(x)  #Exception because x is not defined
  except:
    print("An exception occurred")

  #Many Exceptions
  try:
    print(x)
  except NameError:
    print("Variable x is not defined")
  except:
    print("Something else went wrong")

  #Else - Can use to define a block of code to be executed if no errors were raised
  try:
    print("Hello")
  except:
    print("Something went wrong")
  else:
    print("Nothing went wrong")

  #Finally - If specified, will be executed regardless if the try block raises an error or not.
  try:
    print(x)
  except:
    print("Something went wrong")
  finally:
    print("The 'try except' is finished")

  #This can be useful to close objects and clean up resources:
  #Try to open and write to a file that is not writable:
  try:
    f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
  except:
    print("Something went wrong when opening the file")

  #Raise an exception - same as throw an exception if a condition occurs
  x = -1
  if x < 0:
    raise Exception("Sorry, no numbers below zero")

  #Raise a TypeError if x is not an integer:
  x = "hello"
  if not type(x) is int:
    raise TypeError("Only integers are allowed")

  
  print("Ending <Specific Part> Of Code Challenge")
  print("Ending The Code Challenge")

main()
