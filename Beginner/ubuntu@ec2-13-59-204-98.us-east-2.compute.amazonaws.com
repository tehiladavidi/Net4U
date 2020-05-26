import paramiko
import getpass
from scp import SCPClient
import boto3
from time import sleep
import os


# Connecting to remote machine using Paramiko over SSH

def ssh_cmd(ip, user, password, cmd, host):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username=user, password=password)
    f = open('hostname.txt', "w")
    f.write(host)
    f.close()
    scp = SCPClient(client.get_transport())
    scp.put('hostname.txt', recursive=True, remote_path='/root/')
    scp.close()
    stdin, stdout, stderr = client.exec_command(cmd)
    opt = stdout.readlines()
    opt = "".join(opt)
    return opt


# Exchanging keys with the remote machine

def ssh_keygen(ip):
    os.system('ssh-keygen -t rsa -b 4096 -P "" -f "/root/.ssh/id_rsa"')
    os.system('ssh-copy-id root@{}'.format(ip))
    choose = input("Your keys have been exchanged successfully, would you like to connect? y/n: ")
    if choose == "y" or choose == "Y":
        os.system('ssh root@{}'.format(ip))
    back_to_main()


# Installing required packages on the remote machine

def set_install():
    print("Please hold while we are installing your packages...")
    sleep(1)
    cmd = "cat /root/hostname.txt  > /etc/hostname;" \
          "apt-get install ssh" \
          "apt-get install python3.7 -y;" \
          "apt-get install net-tools -y;" \
          "apt-get install trace-route -y;" \
          "apt-get install sshpass -y;" \
          "apt-get install snmp -y;" \
          "apt-get install python3-pip -y;" \
          "apt-get install apache2 -y;" \
          "pip install paramiko -y;" \
          "pip install boto3 -y;" \
          "apt-get install htop -y;" \
          "apt-get install tree -y;" \
          "apt-get install openjdk-8-jdk -y;" \
          "apt-get install nmap -y;" \
          "apt-get install tcpdump -y;" \
          "apt-get upgrade -y;" \
          "rm -rf /root/hostname.txt;" \
          "reboot"
    return cmd


def ec2():
    ec = boto3.resource('ec2', region_name='us-east-2')
    return ec


def deploy(id, num):
    instance = ec2().create_instances(
        ImageId=id,
        MinCount=1,
        MaxCount=num,
        InstanceType='t2.micro',
        KeyName='tehila_aws_key.pem',
        SecurityGroupIds=['launch-wizard-2'])
    print('New AWS instanceID is : ' + instance[0].id)
    print("----------------------------------------")


def stop():
    show_machines()
    id = input("Enter ID of your virtual machine: ")
    ids = [id]
    while True:
        sure = input("Are you sure that you would like to stop this machine: " + id + "? y/n")
        if sure == "y" or sure == "Y":
            print("Stopping your virtual machine...")
            sleep(3)
            ec2().instances.filter(InstanceIds=ids).stop()
            while True:
                option = input("This virtual machine: " + id + "has been stopped, you would like to stopping"
                                                               " another virtual machine? y/n :")
                if option == "y" or option == "Y":
                    stop()
                elif option == "n" or option == "N":
                    aws_menu()
                else:
                    print("Please type your selection (only y or n): ")
        elif sure == "n" or sure == "N":
            aws_menu()
        else:
            print("Please type your selection (only y or n): ")
            continue


def start():
    show_machines()
    id = input("Enter ID of your virtual machine: ")
    ids = [id]
    while True:
        sure = input("Are you sure that you would like to start this machine: " + id + "? y/n ")
        if sure == "y" or sure == "Y":
            print("Starting your virtual machine...")
            sleep(3)
            ec2().instances.filter(InstanceIds=ids).start()
            while True:
                option = input("This virtual machine: " + id + "has been started, you would like to starting"
                                                               " another virtual machine? y/n :")
                if option == "y" or option == "Y":
                    start()
                elif option == "n" or option == "N":
                    aws_menu()
                else:
                    print("Please type your selection (only y or n): ")
        elif sure == "n" or sure == "N":
            aws_menu()
        else:
            print("Please type your selection (only y or n): ")
            continue


def reboot():
    show_machines()
    id = input("Enter ID of your virtual machine: ")
    ids = [id]
    while True:
        sure = input("Are you sure that you would like to rebooting this virtual machine: " + id + " ? y/n ")
        if sure == "y" or sure == "Y":
            print("Rebooting your virtual machine...")
            sleep(3)
            ec2().instances.filter(InstanceIds=ids).reboot()
            while True:
                option = input("This virtual machine: " + id + "has been rebooted, you would like to rebooting"
                                                               " another virtual machine? y/n :")
                if option == "y" or option == "Y":
                    reboot()
                elif option == "n" or option == "N":
                    aws_menu()
                else:
                    print("Please type your selection (only y or n): ")
        elif sure == "n" or sure == "N":
            aws_menu()
        else:
            print("Please type your selection (only y or n): ")
            continue


def terminate():
    show_machines()
    id = input("Enter ID of your virtual machine: ")
    ids = [id]
    while True:
        destroy = input("This will terminate your virtual machine: " + id + ". Are you sure? y/n : ")
        if destroy == "y" or destroy == "Y":
            print("Terminating your virtual machine...")
            sleep(3)
            ec2().instances.filter(InstanceIds=ids).terminate()
            option = input("This virtual machine: " + id + "has been terminated, you would like to terminate"
                                                           " another virtual machine? y/n :")
            if option == "y" or option == "Y":
                terminate()
            elif option == "n" or option == "N":
                aws_menu()
        elif destroy == "n" or destroy == "N":
            print("Your machine was not deleted")
            aws_menu()
        else:
            print("Please type your selection (only y or n): ")


def show_machines():
    for instance in ec2().instances.all():
        print("\n" + instance.id, ','.join(instance.state))


#             Menu:


def aws_menu():
    choose = input("Menu:\n1. Deploy Virtual Machine\n2. Stop\n3. Start\n4. Reboot\n5. Terminate\n6. show instance"
                   "\n----------------------------------------\nEnter your choose: ")
    dict_image = {1: {'ami-0fc20dd1da406780b': 'Ubuntu'},
                  2: {'ami-0520e698dd500b1d1': 'CentOS'},
                  3: {'ami-04c5bab51cc146925': 'Suse linux'},
                  4: {'ami-067317d2d40fd5919': 'Microsoft windows 2019'}}

    while True:
        print("----------------------------------------")
        if choose == "1":
            while True:
                print("----------------------------------------")
                image_id = int(input(
                    '\nWhich machine you would like to create ?\n1. Ubuntu\n2. CentOS\n3. Suse linux\n4. Microsoft '
                    'Windows 2019 \n----------------------------------------\nEnter your choose: '))
                for key, val in dict_image[image_id].items():
                    id = key
                    name = val
                print("----------------------------------------")
                num = int(input('How many machines you want to deploy: '))
                print("----------------------------------------\nCreating virtual " + name + " machine...")
                sleep(3)
                deploy(id, num)

        elif choose == "2":
            stop()

        elif choose == "3":
            start()

        elif choose == "4":
            reboot()

        elif choose == "5":
            terminate()

        elif choose == "6":
            show_machines()
            while True:
                back = input("Would you like to perform another action? y/n: ")
                if back == "n" or back == "N":
                    break
                elif back == "y" or back == "Y":
                    aws_menu()
                else:
                    continue
            break
        else:
            print("Please type your selection (only 1-5): ")


# Main Menu"

def menu():
    ip = input("Please type the desired IP: ")
    choose = input("Hello! this is your menu. \nPlease choose what you'd like to do: \n"
                   "\n1. Install my key on a remote machine"
                   "\n2. Configure basic installations and packages on my VM"
                   "\n3. Manage AWS machine"
                   "\n4. Install Jenkins master on my VM"
                   "\n5. Install Nagios server"
                   "\n6. Install Netperf tool"
                   "\n"
                   "\nEnter your choice: ")
    if choose == "1":
        ssh_keygen(ip=ip)
    elif choose == "2":
        host = input("Please type the desired hostname: ")
        ssh_cmd(ip, user="root", password=getpass.getpass('Root Password:'), cmd=set_install(),
                host=host)
    elif choose == "3":
        aws_menu()
    elif choose == "4":
        return


def back_to_main(choose):
    choice = "n"
    if choice == "n" or choice == "N":
        print("\nSee you later!")
    else:
        print("\nPlease type y/n only!")
    main = input("\nWould like to perform another action? y/n: ")
    if main == "y" or main == "Y":
        print(choose)
    elif main == "n" or main == "N":
        print("\nSee you later!")
    else:
        print("\nPlease type y/n only!")


menu()
