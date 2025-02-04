#Ch 4 - Lists - Lab #2 - List Indexing

def main():
  #Challenge #1
  print('''
  Can you explain why babylon_5_races[0] = "Centauri"? : index starts from 0
  Can you edit the index to point to "Human" : babylon_5_races[3]
  What is the index for "Human" : 3 ''')
  
  my_string = 'Babylon_5'
  my_list = ['B','a','b','y','l','o','n','_','5'] 
  print(my_string[3:-2])
  print(my_list[3:-2])

  babylon_5_races = ["Centauri", "Minbari", "Narn", "Human", "Shadow", "Vorlon"]

  #Challenge #2
  print(''' Update code by asking the user for an index as an input()
  Can you explain how the variable 'x' is now used as an index? : its a number
  The first race earth contacted, was the "Centauri".
  What index would you use to print "Centauri"? : 0
  Run the code again, but this time select a different race.''')
  
  x = input('enter a index > ')
  x = int(x)
  babylon_5_races = ["Centauri", "Minbari", "Narn", "Human", "Shadow", "Vorlon"]
  print(babylon_5_races[x])
  print(babylon_5_races[0])
  print(babylon_5_races[4])

  #Challenge #3
  print('''
  Run the code again, but this time enter the index -2, then again for -3
  Can you you see the pattern? : The code prints out list.len() + index or just
                                count starting from 1 form the end of the list
  If you were going to print out "Narn" what positive index would you use? 2
  What negative index would you use? -4 ''')

  print(babylon_5_races[-2]) #Shadow
  print(babylon_5_races[-3]) #Human
  print(babylon_5_races[2]) #Narn
  print(babylon_5_races[4]) #Narn


#Challenge #4
 print(''' Using the code you just edited and ran:
 Run the code again, but this time enter the index for the most dangerous and powerful race''')

 print(babylon_5_races[5]) #Vorlon

main()
