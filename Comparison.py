#Ch 2 - Flow Control - Asking Questions - Comparison

def main():
  print(''' This Lab is about Asking Questions and comparing Variables or Objects.
  Is the Answer "TRUE"?

  The == is a comparison to see if 2 variables or objects are equivalent or equal, 
  but there are many other ways to compare objects
      x == y      # x is equal to y
      x != y      # x is not equal to y
      x > y       # x is greater than y
      x < y       # x is less than y
      x >= y      # x is greater than or equal to y
      x <= y      # x is less than or equal to y
      x is y      # x is the same as y
      x is not y  # x is not the same as y
  ''')
  
  print(''' Challenge # 1
  ----------------------------------------------------
  Try changing the values of x and y and see what happens
      
  Hint: https://www.w3schools.com/python/python_operators.asp
  ----------------------------------------------------''')

  print(''' Answer to Challenge 1
  -------------------------------------------------
  Change the values of x and y to see the results of the comparisons''')
  x =  5
  y =  9
  
  print(x == y)  #False
  print(x != y)  #True
  print(x > y)   #False
  print(x < y)   #True
  print(x >= y)  #False
  print(x <= y)  #True
  print(x is y)  #False
  print(x is not y) #True
  
main()
