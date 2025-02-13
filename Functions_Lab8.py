#Ch 3 - Functions - Lab #8 - User Functions - bonjour()

# Functions - Passing Arguments
print('''Functions - Passing Arguments''')      
print('''Challenge #1
Run, then Edit the code in the template example:
      
Can you follow and explain
- How arguments are passed from the main code to the function? : Parameters
- Can you explain how a value is 'returned' : Return statement ''')
def greet(lang):
  if lang == 'es':
    return'Hola'
  elif lang == 'fr':
    return'Bonjour'
  else:
    return'Hello'

def main():
    print(greet('en'),'Glenn')
    print(greet('fr'),'Sabine')
    print(greet('es'),'Carlos')
    
main()

print('''
Challenge #2
Add a few new Languages…
Swahili, Ukrainian, Middle Earth Elven, or maybe Klingon

Challenge #3
Add asking the User for their name and language, then say hi.
      ''')
def greet(lang):
  if lang == 'es':
    return'Hola'
  elif lang == 'fr':
    return'Bonjour'
  elif lang == 'sw':
    return 'Habari'
  elif lang == 'uk':
    return 'Anno'
  else:
    return'Hello'

def main():
  name = input("Enter your name: ")
  language = input("Enter a language: ")
  print(greet(language), name)
  
