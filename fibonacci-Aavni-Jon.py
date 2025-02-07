#Ch 4 - Lists - Lab - fibonacci.py
import random

def main():
  #  my_fibonacci = [0, 1]
  my_fibonacci = []
  #fib_int1 = 4 #This line used to test the code
  fib_int1 = input("Enter an integer from 0-9 : ")

  x = True
  while x :
    try :
      fib_int1 = int(fib_int1)
      x = False
    except :
      print(fib_int1, "is not an integer.")
      fib_int1 = input("Enter an integer from 0-9 : ")
  else :
    fib_int1 +=3
    print("The number is", fib_int1)
    my_fibonacci.append(fib_int1)
    
    fib_int2 = random.randint(1, 20)
    print("The random number is", fib_int2)
    my_fibonacci.append(fib_int2)

    print(my_fibonacci)
    
    for i in range(1, 9):
      fib_sum = fib_int1 + fib_int2
      my_fibonacci.append(fib_sum)
      print(my_fibonacci)
      fib_int1 = fib_int2 
      fib_int2 = fib_sum
    
    print(my_fibonacci)
    print('done')
    
main()
