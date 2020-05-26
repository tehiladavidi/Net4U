dic = {}

for i in range(1, 10):
    print("Hello, please insert your name")
    name = input()

    if name in dic:
        print("This name is already exist!")
    else:
        print("Please insert your phone")
        phone = int(input())
        if phone in dic.values():
            print("Registered you in my list, please change your phone number, you have 2 days")
        dic = {name: phone}


print("Listed in: " + (str(i)))
