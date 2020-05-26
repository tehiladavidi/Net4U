import boto3
from time import sleep
import requests
import os


def ec2():
    ec = boto3.resource('ec2')
    return ec


def deploy(id, num):
    instance = ec2().create_instances(
        ImageId=id,
        MinCount=1,
        MaxCount=num,
        InstanceType='t2.micro',
        KeyName='tehila-aws-key',
        SecurityGroupIds=['launch-wizard-2'])
    print('New AWS instanceID is : ' + instance[0].id)
    print("----------------------------------------")


def stop():
    show_machines()
    id = input("Enter ID of your virtual machine: ")
    ids = [id]
    while True:
        sure = input("Are you sure that you would like to stop this machine: "+id+"? y/n")
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
                    menu()
                else:
                    print("Please type your selection (only y or n): ")
        elif sure == "n" or sure == "N":
            menu()
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
                    menu()
                else:
                    print("Please type your selection (only y or n): ")
        elif sure == "n" or sure == "N":
            menu()
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
                    menu()
                else:
                    print("Please type your selection (only y or n): ")
        elif sure == "n" or sure == "N":
            menu()
        else:
            print("Please type your selection (only y or n): ")
            continue


def terminate():
    show_machines()
    id = input("Enter ID of your virtual machine: ")
    ids = [id]
    while True:
        destroy = input("This will terminate your virtual machine: "+id+". Are you sure? y/n : ")
        if destroy == "y" or destroy == "Y":
            print("Terminating your virtual machine...")
            sleep(3)
            ec2().instances.filter(InstanceIds=ids).terminate()
            option = input("This virtual machine: "+id+"has been terminated, you would like to terminate"
                           " another virtual machine? y/n :")
            if option == "y" or option == "Y":
                terminate()
            elif option == "n" or option == "N":
                menu()
        elif destroy == "n" or destroy == "N":
            print("Your machine was not deleted")
            menu()
        else:
            print("Please type your selection (only y or n): ")


def show_machines():
    for instance in ec2().instances.all():
        print("\n" + instance.id, ','.join(instance.state))


#             Menu:


def menu():
    while True:
        print("----------------------------------------")
        choose = input("Menu:\n1. Deploy Virtual Machine\n2. Stop\n3. Start\n4. Reboot\n5. Terminate\n6. show instance"
                       "\n----------------------------------------\nEnter your choose: ")
        if choose == "1":
            while True:
                print("----------------------------------------")
                imageid = input(
                    '\nWhich machine you would like to create ?\n1. Ubuntu\n2. CentOS\n3. Suse linux\n4. Microsoft '
                    'Windows 2019 \n----------------------------------------\nEnter your choose: ')
                id = []
                name = "none"
                if imageid == "1":
                    id = 'ami-0fc20dd1da406780b'
                    name = "Ubuntu"
                elif imageid == "2":
                    id = 'ami-0520e698dd500b1d1'
                    name = "CentOS"
                elif imageid == "3":
                    id = "ami-04c5bab51cc146925"
                    name = "Suse linux"
                elif imageid == "4":
                    id = "ami-067317d2d40fd5919"
                    name = "Microsoft windows 2019"
                else:
                    print("Enter 1-4 only")
                    break
                print("----------------------------------------")
                num = int(input('How many machines you want to deploy: '))
                print("----------------------------------------")
                print("Creating virtual " + name + " machine...")
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
                    menu()
                else:
                    continue
            break
        else:
            print("Please type your selection (only 1-5): ")


menu()
