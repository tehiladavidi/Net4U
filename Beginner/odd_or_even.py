# (2)  Create a program odd_or_even_numbers.py that asks the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message.

num = int(input("Hello, this program will calculate if your num is even or odd"
                "\nPlease enter your number"))
if num % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")
