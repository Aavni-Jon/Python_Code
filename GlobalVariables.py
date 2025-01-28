#Ch 1 - W3-Schools Review - Variables - Global

#global variable is outside the function
x1 = "awesome"

def myfunc():
  print("Python is " + x1)

myfunc()

#global and local variables print differently depending on where they are created
x2 = "awesome"

def myfunc2():
  x2 = "fantastic"
  print("Python is " + x2)

myfunc2()

print("Python is " + x2)

#make an otherwise local variable global with the global keyword 
def myfunc3():
  global x3
  x3 = "fantastic"

myfunc3()

print("Python is " + x3)

#Changing the global variable inside
x4 = "awesome"

def myfunc():
  global x4
  x4 = "fantastic"

myfunc()

print("Python is " + x4)
