import random

lotto = [random.randint(1, 37)]
man = []
auto = []
check = []
win = []

choice = (int(input("Welcome to lotto! please choose how you'd like to gamble."
                    "\n1.I would like to fill manually"
                    "\n2.I would like to fill automatically"
                    "\n3.I want to check if I won"
                    "\n4.I want to play double lotto")))


    if choice == 1:
        num = (int(input("How much money do you have?")))
        row = num /3
        while row > 0:
            man.append(int(input("Please enter your numbers")))
    elif choice == 2:
        num = (int(input("How much money do you have?")))
        raw = num /3
        auto.append(random.randint(1, 37))
    elif choice == 3:
        check.append(int(input("Please enter your numbers")))
    for i in lotto:
        for j in check:
            if lotto[i] == check[j]:
                win.append(i)
