#Ch 4 - Tuples - Lab #2 - Tuples & Functions

#Challenge 1
def sum_and_avg(t):
    x,y,z = t
    s = x + y + z 
    a = s/3
    return(s, a,)
# see that the type( of the function is <tuple>)
print('--------------------------------------')
print('This is the value of the Tuple returned')
#(sum, avg) = sum_and_avg(3, 16, 7,)
my_tuple = (3, 8, 5,)
x = sum_and_avg(my_tuple)
print(x)
print(type(x))
sum = x[0]
avg = x[1]
print('Sum =', sum)
print('Sum is of type',type(sum))
print('Avg =', avg)
print('Avg is of type',type(avg))
print(type(sum_and_avg(x))

#Challenge 2
def sum_and_avg(t):
  s=0
  for value in t:
    s = s + value
    a = s/len(t)
  return(s, a,)
my_tuple = (1,4,42,84,)
(sum, avg) = sum_and_avg(my_tuple)
print('This is the value of the Tuple returned')
print((sum, avg))
print(type(my_tuple))
print('Sum =', sum)
print('Sum is of type',type(sum))
print('Avg =', avg)
print('Avg is of type',type(avg))

