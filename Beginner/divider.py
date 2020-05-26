# (4)  Create a program divider.py
# that asks the user for a number and then prints out
# a list of all the divisors of that number.
# (If you don’t know what a divisor is,
# it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
dv = []
num = int(input("Hello, this program will calculate the dividers of your number. \nPlease type your number"))


def get_divisors(num):
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            yield i
    yield num
# if div:
#     dv.append(div)
# print(dv)
