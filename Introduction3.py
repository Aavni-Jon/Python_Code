#Ch 2 - Flow Control - Asking Questions Intro - Presentation Lab

def main():
  # Python Lab 1 - Asking Questions - Introduction
  print('''When you are making a variable assignment you use the "=" operator. ''')
  x = 7
  print("x =",x)
  x = 25
  print("x =",x)
  x = 42
  print("x =",x)

  print(''' When you are asking a question, you are performing a comparison,
  and use the "==" operator.The comparison operator == compares two operands 
  and produces "True" if they are equal and "False" if they are not: ''')
  x = 7
  y = 9
  z = 7
  print('x =',x,'  # This is an assignment')
  print('y =',y,'  # This is an assignment')
  print('z =',z,'  # This is an assignment')
  print("(x == z) is",x == z,'  # This is a comparison')
  print("(x == y) is",x == y,'  # This is a comparison')
  print("(z == y) is",z == y,'  # This is a comparison')

  print(''' When asking a question, the answer is Boolean. Boolean means it can 
  only be "TRUE" or "FALSE", 1 or 0. If you are performing a comparison or 
  evaluation, the answer will be Booliean, "TRUE" or "FALSE".  With that answer, 
  you can make program flow decisions. ''')
  x=5
  y=9
  print("The variable or object",x, "is type", type(x))
  print("type(",y,'==',x,") is ",type(y == x))
  print('type(True") is ',type(True))
  print('type(Fasle") is ',type(False))

  print(''' Challenge # 1 
  ----------------------------------------------------
  Can you explain?

  What do the following mean?
  1) Assignment : is the process of giving a value to a variable.
  2) Comparison : is the process of comparing two values to check if they are equal to, 
                  greater than, or less than each other.
  3) Evaluation : is the process of computing the value of an expression or statement; 
                  result is a Boolean.
  4) What is the difference between "=" and "==" : "=' is used to assign a value to a 
                                                  variable; "==" is a comparitson operator.
  5) Boolean : is a data type that can only have two values: True or False; it is used to 
               represent the true value of an expression or statement.
      
  Hint: https://www.w3schools.com/python/python_operators.asp
  ---
  ''')

main()
