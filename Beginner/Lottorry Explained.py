import random
global choose, form, formauth


def manual():
    man = []
    form = []
    num = 0
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
    print(form)
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
    winman = []
    winauth = []
    win = []
    count = 0
    check = double()
    form = manual()
    form_length = len(form)
    i = 0
    j = 0


    for j in range(6):
        num = random.randint(1, 37)
        if num not in win:
            win.append(num)
    print(win)
    while check == 0:
        chose = (int(input("1.Calculate regular manual form"
                           "\n2.Calculate regular automated form")))
        if chose == 1:
            form.sort()
            print(form)
            for k in range(form_length):
                while i < len(form[k]) and j < len(win):
                    if form[k][i] == win[j]:
                        count+=1
                        j+=1
                        i+=1
                    elif form[k][i] > win[j]:
                        i+=1
                    else:
                        j+=1


            winman.append()

        else:


    if check == 1:
        for i in win:
            for j in man:
                while j in man == i in win:
                    winman.append(i)
                print("You've lost, see you next time!")
    if check == 2:
        for i in formauth:
            for j in aut:
                while i in win:
                    winauth.append(i)

            print("You've lost, see you next time!")


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
    return choose


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
