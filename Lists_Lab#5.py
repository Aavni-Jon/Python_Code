#Ch 4 - Lists - Lab #5 - Lists - Append, Extend, Concatenate 

def main():
  # LISTS - Append, Extend, Concatenate
  print('''LISTS - Assigning values by using Append, Extend, Concatenate''')      
  print('''Challenge #1 Fibonacci
  Run, then Edit the code in the template example:
      
  fibonacci_sequence = [0,1,1,2,3, 5, 8, 13, 21, 34]
  Rather than just creating the list with the number, write a program to calculate 
  the fibonacci number and then append, extend and concatenate the sequence
  - See how the append works with fibonacci_sequence[0] + fibonacci_sequence[1]
  - Do this again to append the next value in the sequence.
  - Write a for loop to calcualte and .append 10 more numbers in the sequence. 
    Have the for loop not start at 0.
  - Write a for loop to calcualte and .extend 10 more numbers in the sequence.
    Have this for loop start where the last one left off.''')
  
  fibonacci_sequence = [0,1]
  print(fibonacci_sequence)
  # .append method to Appending to the list
  fibonacci_sequence.append(fibonacci_sequence[0]+fibonacci_sequence[1])
  print(fibonacci_sequence)
  # Use the .append to add the next number in the sequence.
  fibonacci_sequence.append(fibonacci_sequence[1] +fibonacci_sequence[2])
  print(fibonacci_sequence)
  # Use a for loop to calculate and .append 10 more of the next numbers in the sequence
  for i in range(3,12):
    fibonacci_sequence.append(fibonacci_sequence[i-1]+fibonacci_sequence[i])
  print(fibonacci_sequence)
  # Use a for loop to calculate and .extend 10 more of the next numbers in the sequence
  fibonacci_sequence2 = [fibonacci_sequence[len(fibonacci_sequence)-1]] #begins where it ended
  for i in range(0, 9):
    fibonacci_sequence2.append(fibonacci_sequence2[i-1]+fibonacci_sequence2[i])
  fibonacci_sequence.extend(fibonacci_sequence2)
  print(fibonacci_sequence)

main()
