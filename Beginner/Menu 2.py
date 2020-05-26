dic = {}
choice: int = 0
rm = 0
for i in range (5):
    add = input("Let's setup your DNS server! "
            "\nPlease insert your URL address")
    num = input(int("Please insert your IP associated with your URL")


print("Hello! Please choose what you'd like to do: \n1.Add new IP address \n2.Delete an IP address"
      "\n3.Update an IP address \n4.Print all of my address")
if 0 < choice <=4:
    if choice == 1:
        name = (input("Please insert your URL address"))
        IP = (input("Please insert your IP associated with your URL"))
        dic = {add: num}
    elif choice == 2:
        rm = input(int("Please type the address you'd like to delete"))
        if rm in dic:
            del dic[rm]

