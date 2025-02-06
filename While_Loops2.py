#Ch 2 - Flow Control - WHILE

def main():
  #Lab Example # 1 - Using the variable x before it has been assigned
  print(x)

  #Lab Example # 2 - Using the variable x before it has been assigned
  x = x + 1
  print(x)

  #Lab Example # 3 - Using the variable x after it has been assigned
  #x = 0
  x = 7  #x can be initialized to anything
  x = x + 1
  print(x)

  #Lab Example # 4 - short cut increment
  x = 5
  print(x)
  x += 1
  print(x)

  #When the condition is true then the while loop will run
  windows_are_dirty = 0
  while windows_are_dirty > 0 :
    print("Wipe On")
    print("Wipe Off")
  print("Windows are Clean")
  #it will keep running (infinite loop)
  windows_are_dirty = 5
  while windows_are_dirty > 0 :
    print("Wipe On")
    print("Wipe Off")
  print("Windows are Clean")
  #Decrementing the index makes it finite
  windows_are_dirty = 5
  while windows_are_dirty > 0 :
    print("Wipe On")
    print("Wipe Off")
    windows_are_dirty -= 1
  print("Windows are Clean")

  #Lab Example # 5 - Let's Take A Picture
  #n = 5
  n = 10
  print('Say Cheese...')
  while n > 0:
    print(n)
    #n = n - 1 
    #n = n - 2 
    #n = n - 3
    n -= 3
  print("Click!")
  
  #Lab Example # 6 - Infinite Loop
  n = 5
  x = True # Boolean T/F
  print('Say Cheese...')
  while x :
    print(n)
    n = n - 1
  print("Click!")

  #Lab Example # 7 - BREAK
  while True:
    line = input('> ')
    if line == 'done':
      break
    print(line)
  print('Done!')

  #Lab Example # 8 - CONTINUE
  while True:
    line = input('> ')
    if line[0] == '#':
      continue
    if line == 'done':
      break
    print(line)
  print('Done!')

  #Do-While
  x = 5
  y = 3
  while True:
    # Do Something
    print('x =',x,'\ny =',y)
    z = x + y
    print('x + y = ',z)
    #if (z == 8) :
    if (z == 11) :
      break
    x +=1
    print('y is still',y,'but x is now',x)
  print('Done!')

main()
