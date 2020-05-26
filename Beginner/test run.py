import random
import time
def manual():
    man = []
    form = []
    win = []
    num = 0
    count = 0
    check = []
    money = (int(input("How much money do you have?")))
    raw = int(money / 3)
    for i in range(raw):
        for j in range(6):
            num = (int(input("Please enter your numbers between 1-6")))
            while 1 > num > 37 or num in man:
                print("Enter a number between 1-37. Do not duplicate.")
            man.append(num)
            if man not in form:
                form.append(man)
    for j in range(6):
        num = random.randint(1, 37)
        if num not in win:
            win.append(num)
    print("The Winning numbers are: " + str(win))
    print("Let's check if you won \nCalculating...")
    form.sort()
    win.sort()
    for i in range(len(form)):
        counter_new = 0
        for j in range(len(win)):
                if win[j] in form[i]:
                    counter_new=counter_new+1
        print(counter_new)


    print(check)

    return form


def auto():
    aut = []
    formauth = []
    money = (int(input("How much money do you have?")))
    raw = int(money / 3)
    for i in range(raw):
        for j in range(6):
            num = random.randint(1, 37)
            aut.append(num)
            if aut not in formauth:
                formauth.append(aut)
    print(formauth)
    return formauth


def calculate_sum():
    # winman = []
    # winauth = []
    win = []
    # count = 0
    check = 1
    # form_length = len(manual())
    # i = 0
    # j = 0

    for j in range(6):
        num = random.randint(1, 37)
        if num not in win:
            win.append(num)
    print(win)
    if check == 0:
        chose = (int(input("1.Calculate regular manual form"
                           "\n2.Calculate regular automated form "
                           "\n3.Calculate double manual form"
                           "\n4.Calculate double automated form ")))

    elif check == 1:
        form.sort()
        print(form)


def double():
    choose = (int(input("Please choose how you'd like to gamble:\n"
                        "1.I would like to fill manually\n"
                        "2.I would like to fill automatically\n")))
    if choose == 1:
        manual()
    elif choose == 2:
        auto()
    else:
        print("You type wrong number")



def menu():
    while True:
        choice = (int(input("Welcome to lotto! please choose how you'd like to gamble."
                            "\n1.I would like to fill manually"
                            "\n2.I would like to fill automatically"
                            "\n3.I want to check if I won"
                            "\n4.I want to play double lotto")))

        if choice == 1:
            print("Your choice:1")
            manual()

        elif choice == 2:
            print("Your choice:2")
            auto()

        elif choice == 3:
            print("Your choice:3")
            calculate_sum()

        elif choice == 4:
            print("Your choice:4")
            double()

        else:
            print("Please type a number between 1-4 only!")
            continue

        choice2 = (input("Would you like to exit? please type yes/no?"))
        if choice2 == "no" or choice2 == "NO":
            continue
        else:
            print("See you next time!")
            break


menu()
