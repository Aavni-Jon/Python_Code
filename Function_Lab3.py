#Ch 3 - Functions - Lab #3 - ord() & char() - My Name Is... 

# Functions Introduction
def main():
  print('''Functions ord() chr()''')      
  print('''Challenge #1
        
  Hola, Mi nombre es Iñigo Montoya 
  Tú mataste a mi padre. Prepárate a morir
        
  Note the special charaters in the spanish text
        
  Using the Extended ASCII table link --> https://www.ascii-code.com/ and the built-in Functions
  - ord()    - convert a number or character to it's unicode value
  - chr()    - convert a unicode value to it printable character
  
  Using the chr() function, complete the sentence with the correct 
  accented characters in the 2nd line in the example above.   ''')
  print(''' Enter Your Code Here:
  ----------------------------------------------------''')
  
  print('Hola, Mi nombre es I' + str(chr(0xf1)) + 'igo Montoya')
  print('T' + str(chr(ord('ú'))) + ' mataste a mi padre. Prep' + str(chr(ord('á'))) +'rate a morir')
  print('Done with Challenge 1')

main()
