#Ch 3 - Functions

#Built-in functions
def main():
  #type()
  print('Using the function type()')
  my_var_1 = 42
  x = type(my_var_1)
  print(x)
  
  print('Using the function type()')
  my_var_2 = 'a long string of words'
  print(type(my_var_2))
  print(my_var_2)

  #len()
  print('Using the function len()')
  my_var_2 = 'a long string of words'
  print(len(my_var_2))
  print(my_var_2)

  #max() & min()
  print('Using the function max()')
  my_var_2 = 'a long string of words'
  bigger = max(my_var_2)
  print(bigger)
  print('Using the function min()')
  smaller = min(my_var_2)
  print(smaller)
  print('done')

  #ord()
  print('Using the function ord()')
  x = ord('w')
  print(x)

  #chr()
  print('Using the function chr()')
  x = chr(119)
  print(x)

  #int(), type(), and id()
  print('Using the function int() & type() & id()')
  user_input = input('enter a number > ')
  print(user_input)
  print(type(user_input))
  print('the id() of user_input as a str', id( user_input))
  print(ord(user_input))
  user_input = int(user_input)
  print(type(user_input))
  print('the id() of user_input as a int', id( user_input))
  
main()

#Building your own functions
def print_lyrics():
  print("Tonight you're falling in love")
  print("Let me go now")
  print("This feeling's tearing me up")
  print("Here we go now")
  print("Come on,")

def print_chorus():
  print("Shake, shake")
  print("Shake, shake, shake it")

def main2() :  
  print('Part of Shake it by Metro Station')
  print_lyrics()
  print_chorus()
  print_chorus()
  print_chorus()
  print_chorus()
  print_chorus()
  
main2()

#Passing and Returning arguments, Using parameters
def greet():
  return "Hello"
print(greet(), "Glenn")
print(greet(), "Sally")

def my_add(x,y) :
  z = x + y
  return z
my_num_1 = 5
my_num_2 = 2
sum = my_add(my_num_1, my_num_2)
print(sum)

#Be Fruitful - returning something
def greet2(lang):
  if lang == 'es':
      return'Hola'
  elif lang == 'fr':
      return'Bonjour'
  else:
      return'Hello'

def main3():
  print(greet2('en'),'Glenn')
  print(greet2('fr'),'Sabine')
  print(greet2('es'),'Carlos')
    
main3()


#A program that calls a function to convert Dollars to another currency. 
US$ to CAN$ is 1.27.  so if you have $10 US dollars, that would convert into $12.70 Canadian.  
That same $10 US would be $278.40 New Taipei Dollars, as the conversion from US dollars is 27.84
def currencyConversion(x):
  return x*1.43

def main4():
  x = float(input("Enter a number: "))
  print(x, "US dollars is equal to", currencyConversion(x), "Canadian dollars")
main4()

