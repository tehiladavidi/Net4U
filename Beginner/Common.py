# (5)  Create a program common_list.py
# that takes two lists:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and returns a list that contains only the elements that
# are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
#
#
#
def Diff(a, b):
    return list(set(a) - set(b))


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
print(Diff(a, b))
