man = []
num = []
money = 0
row = []


money = (int(input("Please enter how much money do you have")))
line = int(money / 3)
for i in range(line):
    for j in range(6):
        num.append(int(input("Please inset your numbers")))
    row.append(num)
    print(row)
