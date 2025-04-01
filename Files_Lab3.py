#Ch 9 - Files - Lab #3 - Reading Lines

# Opening File Handles and reading data from files
print('''
This Lab is about opening a file handle, and reading 
the file, line by line using the file method: 
- file_handle = open(file_name) method
      ''')
# Challenges
print('''
Challenge #1 & #2
----------------------------------------------------
#1 - Edit the code below to count each line, 
     and print the total out at the end
      
#2 - Edit the code below to open the text-file-mail-short.txt file
---
''')
# -------------------------------------------------
print('''Answer to Challenges
-------------------------------------------------''')
# -----------------------------
fhand = open('text-file-matrix.txt')
# You need a variable to count the lines
count = 0 #Challenge 1
for line in fhand:
    # You need to increment the line count Variable
  count = count + 1 #Challenge 1
	print(line)
print('Line Count:', count)
#Challenge 2
f2 = open('text-file-mail-short.txt')
for line in f2:
	print(line)
print('''
-------------------------------------------------''')
