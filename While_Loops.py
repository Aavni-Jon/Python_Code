#Ch 2 - W3-Schools Review - Flow Control - While Loops
#https://www.w3schools.com/python/python_while_loops.asp


def main():
  print("Starting The Code Challenge")
  # Declare Any main() Variables - (Not Global)

  print("Starting <Specific Part> Of Code Challenge")
  # Enter Your Code Here:
  print('Enter Your Code Here:')
  x = 42
  print(x)

  #while loop
  i = 1
  while i < 6:
    print(i)
    i += 1

  #break statement
  i = 1
  while i < 6:
    print(i)
    if i == 3:
      break
    i += 1

  #continue statement
  i = 0
  while i < 6:
    i += 1
    if i == 3:
      continue
    print(i)

  #else statement
  i = 1
  while i < 6:
    print(i)
    i += 1
  else:
    print("i is no longer less than 6")
  
  print("Ending <Specific Part> Of Code Challenge")
  print("Ending The Code Challenge")

main()
