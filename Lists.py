#Ch 4 - W3-Schools Review - Lists
#https://www.w3schools.com/python/python_lists.asp

def main():
  #Creating a list
  thislist = ["apple", "banana", "cherry"]
  print(thislist)

  #Allow Duplicates
  thislist = ["apple", "banana", "cherry", "apple", "cherry"]
  print(thislist)

  #List Length
  thislist = ["apple", "banana", "cherry"]
  print(len(thislist))

  #List Items - Data Types
  list1 = ["apple", "banana", "cherry"]
  list2 = [1, 5, 7, 9, 3]
  list3 = [True, False, False]
  list4 = ["abc", 34, True, 40, "male"]

  #type()
  mylist = ["apple", "banana", "cherry"]
  print(type(mylist))

  #The list() Constructor
  thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
  print(thislist)


main()

