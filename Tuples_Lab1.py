#Ch 4 - Tuples - Lab #1 - Tuples Introduction

#Challenge 1
def sum_and_avg(t):
    x,y,z,zz = t
    s = x + y + z +zz
    a = s/4
    return(s, a,)
# see that the type( of the function is <tuple>)
print('--------------------------------------')
print('This is the value of the Tuple returned')
#(sum, avg) = sum_and_avg(3, 16, 7,)
my_tuple = (2, 9, 42,76,)
x = sum_and_avg(my_tuple)
print(x)
sum = x[0]
avg = x[1]
print('Sum =', sum)
print('Sum is of type',type(sum))
print('Avg =', avg)
print('Avg is of type',type(avg))
print(type(sum_and_avg(x))

#Challenge 2
def sum_and_avg(t):
    x,y,z = t 
    s = x + y + z
    a = s/3
    return(s, a,)
my_tuple = (2,6,42,)
print('My Tuple =', my_tuple)
print('my_t is of type',type(my_tuple))
(sum, avg) = sum_and_avg(my_tuple)
print('Sum =', sum)
print('Sum is of type',type(sum))
print('Avg =', avg)
print('Avg is of type',type(avg))

#Challenge 3
def sum_and_avg(t):
  x,y,z = t 
  for value in range(len(t)):
    s = x + y + z
    a = s/3
    return(s, a,)
(sum, avg) = sum_and_avg(my_tuple)
print('This is the value of the Tuple returned')
print((sum, avg))
print(type(my_tuple))
print('Sum =', sum)
print('Sum is of type',type(sum))
print('Avg =', avg)
print('Avg is of type',type(avg))
