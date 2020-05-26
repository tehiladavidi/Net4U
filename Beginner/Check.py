# #import random modules
import random
from time import sleep
from random import randint

print("Hello, Welcome to our Casino!")

# #generate random integer values
print("Now we will roll the dices...")
sleep(3)
num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
sum = 0

if num1 == num2 and num1 + num2 == 6:
    sum = 100
    print("You have won 100$!")

elif num2 != num1:
    if num1 == 1 or num2 == 2:
        sum = 15
    print("You have won 15$!")

else:
    print("You have lost, try again next time!")


print("Calculating...")
sleep(3)
print("Your Balance: %s$" % (sum))
