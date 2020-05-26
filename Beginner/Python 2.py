IP = input("Hello, this program will validate your IP address. Please type your IP: ")
add = list(IP.split("."))
print(add)
for i in len(add):
    if 1 < int(add[i]) > 255:
        print("Your IP is valid")
else:
    print("Your IP not valid")
