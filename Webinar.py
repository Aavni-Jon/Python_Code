#Python In An Hour Webinar
#https://register.gotowebinar.com/recording/8025969087427809538

#the following code was done in a shell, completed in the slides shown in the video
2 + 2
a = 2
b = 3
a*b
print("Hello world")
for i in range(4): print(i)
n = 2
for i in range(8)
  n = n * n
  print(n)

7/3 #integer division
7//3 #Floor division (truncate)
7%3 #Remainder division
2**6 #Exponentiation

round(6.6666666, 2)
str(45.67) #convert to string
int('999') #convert to integer
hex(255) #convert to hex

'abc' + 'def' #Concatenation
s = """A multi-line string"""
len(s) #Length of string

s = 'abcdef'
s[0] #index - 1st character
s[1] #index - 2nd character
s[-1] #index - last character
s[-2] #index - 2nd to last character

s[2:4] #slice --> upper bound is exclusive
s[:3] #start defaults to 0
s[3:} #stop defaults to length
s[1:6:2] #step --> starts at index 1 and steps by 2, stop at 6

'abcdef'[-1] #index
'abcdef'[0:3] #slice
'abcdef'.upper() #Method call --> all become uppercase
'abcdef'.find('cd') #Method call --> returns index
'abcdef'.find('gg') #Not found --> returns -1
'abcdef'[6] #Exception

if a == 0:
  b = 1
  if c < 0 and d > 0:
    b = 2
  elif a > 0:
    b = 3
  else:
    for i in range(4): #0 1 2 3
      b = 4
      while b > 0:
        print(b)
        b = b - 1
      if i == j: break #jump out of for loop

#Comparison operators: < > == >= <= !=
#Boolean operators: and or not
#Arithmetic operators: + - * / // % **
#Bitwise operators ~ & | >> <<
#Assignment operators = += -= *= /= //= %= **=
#Membership/Identity operators in  not in  is  is not

#Conditional Statements
x = a if b < x else d + e
if b < c:
  x = a
else: 
  x = d + e

#Range
for i in range(4):
  print(i, end = ' ') #end means to separate each line with a space instead of new line
for i in range(2, 6): #prints 2 3 4 5
  print(i, end = ' ')
for i in range(0, 8, 2): #prints 0 2 4 6
  print(i, end = ' ')

#Function
def add(p, q, r):
  temp = p + q + r
  return temp
sum = add(1, 10, 100)
a, b, c = 1, 10, 100 #global variables
def printsum(): #no arguments, no return value
  print(a + b + c)
printsum()

#list
a = [1, 2, 3]
a[0]
b = [1, True, a, 'four']
b
b[-1] #index
b[0:2] #slice

#Tuple - are immutable lists
def um_and_diff(a, b):
  return (a + b, a - b)
x = sum_and_diff(7, 4)
print(x)
x[0] = 0 #Type error, tuples are read-only

#Some list methods
x = [] #empty list
x.append('a') 
x
x.append('b')
x
x.insert(1, 'c')
x
x.pop() # returns final value in list
x #removes the values that was popped

#iterator - returns one value at a time
s = [1, 2, 3]
it = iter(s)
it
#return values
next(it)
next(it)
next(it)
next(it) #Error bc no more values

#Loops and lists (example of iterator)
who = ['Tom', 'Dick', 'Harry']
for w in who:
  print('Hello ' + w)

#Generator - A function that uses yield
def generator(n):
  for i in range(n):
    yield 100 + i
it = generator(4) #loops 4 times
for i in it: print(i) 

#list comprehensionm
s = []
for i in range(1, 6):
  s.append(i*i)
print(s)
t = [i*i for i in range(1, 6)] #llst comprehension
print(t)
pairs = [(i, j) for i in range(3)
                for j in range(3) if i != j]
print(pairs) #prints [(0,1), (0,2), (1,0), (1,2), (2,0), (2,1)] -- list of tuples

#Files
#writing
filename = 'spam.txt'
file = open(filename, 'w') #'w' = write, 'r' = read, 'r+' = read or modify, 'a' = append
file.write('Monty\n')
file.write('Python\n')
file.close()
#reading
with open('spam.txt') as file: #with is a context manager
  for line in file: #line is a text string in the file
    print(line, end='')

#Class
class Coord:
  def __init__(self, x, y): #built-in methods start and end with two _
    self.x = x
    self.y = y
  def get(self):
    return (self.x, self.y)
  def add(self, other):
    return Coord(self.x + other.x, self.y + other.y)
c1 = Coord(1, 1) #instance object
c2 = Coord(2, 3) #instance object
c3 = c1.add(c2) #Method call -- only 1 argument, passes to first argument

#Standard Library
import math
n = math.log2(1024)

import random
r = random.random()

import datetime
d = datetime.datetime.now()

import time
t1 = time.process_time()
t2 = time.process_time()
delta = t2 - t1

import os
c = os.getcwd() #returns current working directory
d = os.listdir() # returns content of directory 

import subprocess
subprocess.run('copy test.py foo.py', shell = True, check = True)

