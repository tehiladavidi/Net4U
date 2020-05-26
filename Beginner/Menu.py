import random
from random import randint

print("Hello, this is our menu! \n1.This will calculate the power of two numbers you'll insert"
      "\n2.Let's roll the dices! \n3.Show me my personal details \n4.Check if my IP is available")
choice = int(input("Please type any number between 1-4"))

if 0 < choice <= 4:
    if choice == 1:
        a = int(input("Please enter the first num"))
        b = int(input("Please enter the secound num"))
        print(a ** b)
    elif choice == 2:
        q1 = random.randint(1, 5)
        q2 = random.randint(1, 5)
        print(str(q1))
        print(str(q2))
    elif choice == 3:
        print("Your Name is:Tehila Davidi \nYour Phone is:0509915262 \nYour Email is:tehiladavidi@gmail.com")
    elif choice == 4:
        new_ip = input("Please insert your IP address")
        my_list = ['172.16.1.1', '172.16.1.2', '172.16.1.3', '172.16.1.4']
        if new_ip in my_list:
            print("IP exist, please choose a new one")
        else:
            my_list.append = new_ip
else:
    print("Please inset a choice only between 1-4")
