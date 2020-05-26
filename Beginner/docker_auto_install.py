#!/bin/python3.7
from time import sleep
import os


# Docker Installation ###
def Installation():
    print("This Script Will Install Docker And Pull Nginx & Centos Images")
    sleep(1)
    print("Starting With Docker")
    sleep(1)
    os.system("curl - fsSL https: // get.docker.com - o get - docker.sh")
    os.system("bash get - docker.sh")
    print("Docker Installation is Done")
    sleep(1)


# Pulling Nginx & Centos Images ###
def Pull():
    print("Starting Pulling Nginx & Centos Images")
    sleep(1)
    os.system("sudo docker pull nginx")
    os.system("sudo docker pull centos")
    print("Nginx & Centos images are pulled successfully")
    sleep(1)
    os.system("sudo docker images")


# Deploy Images ###
def Deploy():
    while 1:
        choice = input('''
                        Choose The Image You'd Like To Deploy:
                        1) Deploy Nginx.
                        2) Deploy Centos.
                           ''')
        if choice == "1":
            container = input("How many Containers Would you like to Deploy")
            for i in container:
                os.system("sudo docker run -d  `sudo docker images | grep nginx | awk 'NR==1 {print $3}'`")
                print(i, "Done!")
        elif choice == "2":
            container = input("How many Containers Would you like to Deploy")
            for i in container:
                os.system("sudo docker run -d  `sudo docker images | grep centos | awk 'NR==1 {print $3}'`")
                print(i, "Done!")
        os.system("sudo docker ps -a")


# Getting Images Info ###
def info():
    print("Klum")
    # os.system("echo "nginx: `sudo docker images | grep nginx | awk 'NR==1 {print $3}'`" >> /home/shaked/Desktop/Docker/containers.txt")
    # os.system("echo "centos: `sudo docker images | grep centos | awk 'NR==1 {print $3}'`" >> /home/shaked/Desktop/Docker/containers.txt")
    # os.system("cat /home/shaked/Desktop/Docker/containers.txt")


# Delete Images ###
def Delete():
    while 1:
        choice = input('''
                        Choose The Image You'd Like To Deploy:
                        1) Delete Nginx.
                        2) Delete Centos.
                           ''')
        if choice == "1":
            quan = input("How many Containers Would you like to Delete?")
            for i in quan:
                os.system("sudo docker stop  `sudo docker ps -a | grep nginx | awk 'NR==1 {print $1}'`")
                os.system("sudo docker rm  `sudo docker ps -a | grep nginx | awk 'NR==1 {print $1}'`")
                print(i, "Done!")
        elif choice == "2":
            quan = input("How many Containers Would you like to Delete?")
            for i in quan:
                os.system("sudo docker stop  `sudo docker ps -a | grep bash | awk 'NR==1 {print $1}'`")
                os.system("sudo docker rm  `sudo docker ps -a | grep bash | awk 'NR==1 {print $1}'`")
                print(i, "Done!")
        os.system("sudo docker ps -a")


# Main Menu ###
def main():
    while 1:
        choice = input('''
               Docker Menu:
               1) Install Docker.
               2) Pull Images.
               3) Deploy Images.
               4) Get Info
               5) Delete Images.
               ''')
        if choice == "1":
            Installation()
        if choice == "2":
            Pull()
        if choice == "3":
            Deploy()
        if choice == "4":
            info()
        if choice == "5":
            Delete()


main()
