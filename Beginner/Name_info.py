# (1)  Create a program name_info.py that asks the user to enter their name and their age.
# # Print out a message addressed to them that tells them the year they were born in.

from datetime import date

# date object of today's date
today = date.today()
year = today.year


name = (input("Hello, this program will calculate the year you were born."
              "\nPlease enter your name"))
age = (int(input("Please enter your age")))
birth_year = year - age
print(name+str(", the year you were born is: " + str(birth_year)))
