#Ch 9 - Files - Lab #6 - Reading & Finding

# Finding Stuff
# You can get the following file with wget
# sudo wget -O text-flie-matrix.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-matrix.txt
# sudo wget -O text-file-mail-very-short.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-mail-very-short.txt
# sudo wget -O text-file-mail-short.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-mail-short.txt
# sudo wget -O text-file-mail-long.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-mail-long.txt

print('''
Use the String Methods to find stuff

  1) Can you find all the lines that start with "From:"
  2) What about line that start with "To:"
  3) Find all the lines with an email addresses
    - How would you find them?
    - Hint: split the line into a list of "words" then look for emails
  4) Dates? Can you find the line with the oldest "Date" 'Date: 2008-01-04 11:11:00 -0500 (Fri, 04 Jan 2008)'
    - Same Hint as 3
      
      ''')
xfile = open('text-file-mail-very-short.txt')
#oldest date
  oldest_date = None
  oldest_line = None

for line in xfile:
  #1
  if line.startswith("From:"):
    line=line.rstrip()
    print(line)
  #2
  if line.startswith("To:"):
    line=line.rstrip()
    print(line)
  #3
  if line.startswith("From:"):
    line=line.rstrip()
    line = line.lstrip("From: ")
    print(line)
  '''words = line.split()
  for word in words:
    foundAt = word.find('@')
    foundPeriod = word.find('.')
    if foundAt != -1: and foundPeriod != -1:
      line=line.rstrip()
      print(word)
  '''
  #4
  if line.startswith('Date'):
    line=line.rstrip()
    print(line)
  #oldest date
  for word in words:
    parts = word.split('-')
    if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
      year = int(parts[0]) 
      month = int(parts[1])
      day = int(parts[2])
      date_str = str(year) + '-' + str(month).rjust(2, '0') + '-' + str(day).rjust(2, '0')
      if oldest_date is None or (year, month, day) < oldest_date:
        oldest_date = (year, month, day)
        oldest_line = line

if oldest_line:
    oldest_date_str = str(oldest_date[0]) + '-' + str(oldest_date[1]).rjust(2, '0') + '-' + str(oldest_date[2]).rjust(2, '0')
    print("\nThe line with the oldest date is: " + oldest_line.strip())
    print("Oldest date found: " + oldest_date_str)
else:
    print("No valid date found in the file.")
