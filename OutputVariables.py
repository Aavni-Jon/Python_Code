#Ch 1 - W3-Schools Review - Variables - Output Variables

def main():
 #Use print() 
  x = "Python is awesome"
  print(x)

#Output multiple by separating with a comma
  x = "Python"
  y = "is"
  z = "awesome"
  print(x, y, z)

 #'+' can also be used to output multiple varibales
 #need spaces after the words because otherwise it join it as one word
  x = "Python "
  y = "is "
  z = "awesome"
  print(x + y + z)

 #'+' works as a mathematical operator for numbers
  x = 5
  y = 10
  print(x + y)

 #'+' combinging a string and a number causes and error
  x = 5
  y = "John"
  print(x + y)

#A comma can support multiple data types
  x = 5
  y = "John"
  print(x, y)

#Test
  print("Hi", 1 + 2, "Bye" + " Bye" , 2) #prints 'Hi 3 Bye Bye 2'

main()
