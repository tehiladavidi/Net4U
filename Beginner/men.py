#!/bin/python3


import boto3
from time import sleep
import requests
import os


def ec2():
    ec2 = boto3.resource('ec2')

    return ec2


def deploy(id, num):
    instance = ec2().create_instances(
        ImageId=id,
        MinCount=1,
        MaxCount=num,
        InstanceType='t2.micro',
        KeyName='netanelkey',
        SecurityGroupIds=['launch-wizard-2'])
    print('New AWS instanceID IS : ' + instance[0].id)


def stop():
    show_machins()
    id = input('enter id: ')
    ids = [id]
    ec2().instances.filter(InstanceIds=ids).stop()


def start():
    show_machins()
    id = input('enter id: ')
    ids = [id]
    ec2().instances.filter(InstanceIds=ids).start()


def reboot():
    show_machins()
    id = input('enter id: ')
    ids = [id]
    ec2().instances.filter(InstanceIds=ids).reboot()


def terminate():
    show_machins()
    id = input('enter id: ')
    ids = [id]

    ec2().instances.filter(InstanceIds=ids).terminate()


def show_machins():
    for instance in ec2().instances.all():
        print("\n" + instance.id, ','.join(instance.state))

        ## Menu ##


def menu():
    while True:
        choose = input(
            "Menu:\n1. Deploy Virtual Machine\n2. Stop\n3. Start\n4. Reboot\n5. Terminate\n6.show instance\nEnter your "
            "choose: ")
        if choose == "1":
            while True:
                imageid = input(
                    '\nWhich machine you would like to create ?\n1.Ubuntu\n2.CentOS\n3.Suse linux\n4.Microsoft Windows '
                    '2019 '
                    '\nEnter your choose: ')
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
                num = int(input('How machines you want to deploy : '))
                print("Creating virtual " + name + " machine...")
                sleep(3)
                deploy(id, num)

        elif choose == "2":
            print("Stopping your virtual machine...")
            sleep(3)
            stop()

        elif choose == "3":
            print("Starting your virtual machine...")
            sleep(3)
            start()

        elif choose == "4":
            print("Rebooting your virtual machine...")
            sleep(3)
            reboot()

        elif choose == "5":
            destroy = input("This will terminate your virtual machine. Are you sure? y/n : ")
            if destroy == "y" or destroy == "Y":
                sleep(3)
                terminate()
            elif destroy == "n" or destroy == "N":
                print("Your machine was not deleted")
                menu()
            else:
                print("Please type your selection (only y or n): ")

        elif choose == "6":
            show_machins()
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
            print("enter 1-5 only")


menu()
