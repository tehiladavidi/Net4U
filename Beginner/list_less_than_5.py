# 3)  Create a program list_less_than_5.py
# use this list:
# ages = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Write a program that creates a new list that has all the elements
# less than 5 from ages list and print out all the elements of the new list.

ages = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_5 = []
temp = []
x = 0
for x in ages:
    if x < 5:
        less_than_5.append(x)
    less_than_5 = list(dict.fromkeys(less_than_5))
print(less_than_5)
