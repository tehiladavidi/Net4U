# #import random modules
import random
from time import sleep
from random import randint

print("Hello, Welcome to our Casino!")
# #generate random integer values
print("Now we will roll the dices...")
sleep(3)
q1 = random.randint(1, 6)
q2 = random.randint(1, 6)
a = 0
b = 0
c = 0
if q1 == q2 and q1 + q2 == 6:
    a = 100
    print("You have won 100$!")
elif q2 != q1 and q2 == 2:
    b = 15
    print("You have won 15$!")
elif q2 != q1 and q1 == 1:
    c = 15
    print("You have won 15$!")
else:
    print("You have lost, try again next time!")

if a > 0 or b > 0 or c > 0:
    print("Calculating...")
    sleep(3)
    print("Your Balance: %s$" % (a + b + c))
else:
    print("Your Balance: 0$ ")

print(str(q1))
print(str(q2))
