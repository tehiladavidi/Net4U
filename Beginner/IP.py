ip_list=[]
ip_list.append((input("Enter First IP")))
ip_list.append((input("Enter 2nd IP")))
ip_list.append((input("Enter 3rd IP")))
ip_list.append((input("Enter 4th IP")))
ip_list.append((input("Enter 5th IP")))

print("\nThis is the list: "+ str(ip_list))

new_ip=input("Enter new ip address")

if (new_ip in ip_list):
    print("IP Address Already exist")
else:
    ip_list.append(new_ip)

    print(len(ip_list))

