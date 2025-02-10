#Ch 3 - Functions - Lab #4 - More Built In Functions
'''Challenge #1

Write some code that uses the following built-in functions
Run, then Edit the code in the template example:
      
Using some built-in Functions

abs()    - try some equation like x=(4+5)*-7
bin()    - change a decimal number to it's Binary
hex()    - change a decimal number to it's Hex value
chr()    - convert a unicode value to it printable character
round()  - Do some math, get a long floating point number and round it.  Then round it to 2 significant digits
Pick 3 more functions and try them...
Still have time, pick 3 more      '''

def main():
  #abs()
  x = (4+5)* -7
  print(abs(x))
  
  #bin()
  x = 4.6
  print(bin(x))
  
  #hex()
  print(hex(x))
  
  #chr()
  x = 398
  print(chr(x))
  
  #round()
  x = round(5.76543, 2)
  print(x)
  
  #reversed()
  x = [1, 4, 3, 2]
  x2 = reversed(x)
  for i in x2:
    print(i)
  
  #sorted()
  print(sorted(x))
  
  #slice()
  x = [1, 4, 3, 2]
  x2 = slice(2)
  print(x[x2])
  
  #sum()
  print(sum(x))
  
  #setattr()
  class Person:
    name = "John"
    age = 36
    country = "Norway"
  setattr(Person, 'age', 40)
  # The age property will now have the value: 40
  x = getattr(Person, 'age')
  print(x)
  
  #bool()
  x = 20
  print(bool(x))
  
main()
