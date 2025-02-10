#Ch 3 - Functions - Lab #5 - ord() & char() - Ohms Law
#Functions Introduction - Using, Finding and Printing Special Extended ASCII Characters
#Ohms Law - Ohms - Ω"
'''Challenge #1     
- ord()    - convert a number or character to it's unicode value
- chr()    - convert a unicode value to it printable character

Using the ord() function find the hex value for the 'Ω' symbol.
Write a electronics equation showing Ohms law where you print out the calculation for the resistance of a circuit with 5 volts and 20mA
With the variables volts=? and current =?, using the values of 5 for volts and 20mA for current, calculate the Resistor value and print the Ω using the chr() function
example output>> A circuit with a voltage of 5v and a current of 20mA will require a resistor of 250Ω
Update your program that will ask the user for a Voltage and Current, and calculate the Resistor value and print the Ω using the chr() function  
'''

def main():
  volts = 5
  current = 20
  resistance = volts/current*1000
  print("A circuit with a voltage of 5v and a current of 20mA will require a resistor of", resistance, chr(ord('Ω')))

  volts = int(input("Enter a number for volts: "))
  current = int(input("Enter a number for current: "))
  resistance = volts/current*1000
  print("A circuit with a voltage of " + str(volts) + "v and a current of " + str(current) + 
        "mA will require a resistor of " + str(resistance) + chr(ord('Ω')))

main()

