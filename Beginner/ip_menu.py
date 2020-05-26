from time import sleep
import boto3
import getpass
import os
import paramiko
from scp import SCPClient
import re


# Connecting to remote machine using Paramiko over SSH

def ssh_cmd(ip, user, password, cmd, host):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username=user, password=password)
    if host is not None:
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
    elif choose == "n" or choose == "N":
        print("See you later!")
    else:
        print("Please type y/n only!")
    main = input("Would like to perform another action? y/n: ")
    if main == "y" or main == "Y":
        menu()
    elif main == "n" or main == "N":
        print("See you later!")
    else:
        print("Please type y/n only!")


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


def deploy():
    print("----------------------------------------")
    print("Welcome to deploy menu!")
    dict_image = {1: {'ami-0fc20dd1da406780b': 'Ubuntu'},
                  2: {'ami-0520e698dd500b1d1': 'CentOS'},
                  3: {'ami-04c5bab51cc146925': 'Suse linux'},
                  4: {'ami-067317d2d40fd5919': 'Microsoft windows 2019'}}

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
    instance = ec2().create_instances(
        ImageId=id,
        MinCount=1,
        MaxCount=num,
        InstanceType='t2.micro',
        KeyName='tehila-aws-key',
        SecurityGroupIds=['launch-wizard-1'])
    print('New AWS instanceID is : ' + instance[0].id)
    print("----------------------------------------")
    while True:
        action = input("Would you like to perform another action? y/n: ")
        if action == "n" or action == "N":
            menu()
        elif action == "y" or action == "Y":
            aws_menu()
        else:
            print("Please type your selection (only y/n): ")
            continue


def stop():
    print("Welcome to stopping menu!")
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
    print("Welcome to start menu!")
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
    print("Welcome to reboot menu!")
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
    print("Welcome to terminate menu!")
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
    print("These are your machines: ")
    for instance in ec2().instances.all():
        print("\nMachine ID: " + ("".join('{}'.format(k) for k, in instance.id)))
        for v in instance.state.items():
            print(str(v[0] + ': ' + str(v[1])))


#             AWS-Menu:


def aws_menu():
    while True:
        print("----------------------------------------")
        print("Welcome to AWS menu! \nPlease choose what you'd like to do: "
              "\n----------------------------------------")
        line = input("Menu:\n1. Deploy Virtual Machine\n2. Stop\n3. Start\n4. Reboot\n5. Terminate\n6. Show machines"
                     "\n----------------------------------------\nEnter your choose: ")
        dict_choose = {'1': deploy, '2': stop, '3': start, '4': reboot, '5': terminate,
                       '6': show_machines}
        lines = ["1", "2", "3", "4", "5", "6"]

        if line in lines:
            functionToCall = dict_choose[line]
            functionToCall()


def install_jenkins():
    print("For installing Jenkins, we need to prepare the environment \nto make sure it will go smoothly.")

    cmd = "apt-get install nginx -y;" \
          "apt-get install openjdk-8-jdk -y;" \
          "wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add - ;" \
          "sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list' ;" \
          "apt-get update -y;" \
          "apt-get install jenkins -y;" + set_install()
    return cmd


def install_nagios():
    cmd = "apt-get update;" \
          "apt-get install curl -y;" \
          "apt install autoconf gcc make unzip libgd-dev libmcrypt-dev libssl-dev dc snmp libnet-snmp-perl gettext -y;" \
          "cd ~;" \
          "curl -L -O https://github.com/NagiosEnterprises/nagioscore/archive/nagios-4.4.4.tar.gz;" \
          "tar zxf nagios-4.4.4.tar.gz;" \
          "cd nagioscore-nagios-4.4.4;" \
          "./configure --with-httpd-conf=/etc/apache2/sites-enabled;" \
          "make all;" \
          "make install-groups-users;" \
          "make install;" \
          "make install-daemoninit;" \
          "make install-commandmode;" \
          "make install-config;" \
          "make install-webconf;" \
          "a2enmod rewrite;" \
          "a2enmod cgi;" \
          "usermod -a -G nagios www-data;" \
          "htpasswd -b -c /usr/local/nagios/etc/htpasswd.users nagiosadmin nagios123;" \
          "systemctl restart apache2;" \
          "cd ~;" \
          "curl -L -O https://nagios-plugins.org/download/nagios-plugins-2.2.1.tar.gz;" \
          "tar zxf nagios-plugins-<^>2.2.1<^.tar.gz;" \
          "cd nagios-plugins-2.2.1;" \
          "./configure;" \
          "make;" \
          "make install;" \
          "cd ~;" \
          "curl -L -O https://github.com/NagiosEnterprises/nrpe/releases/download/nrpe-3.2.1/nrpe-3.2.1.tar.gz;" \
          "tar zxf nrpe-3.2.1.tar.gz;" \
          "cd nrpe-3.2.1;" \
          "./configure;" \
          "make check_nrpe;" \
          "make install-plugin;"
    return cmd


# Docker Installation
def Installation(ip):
    print("This Script Will Install Docker And Pull Nginx & Centos Images")
    sleep(1)
    print("Starting With Docker")
    sleep(1)
    ssh_cmd(ip, user="root", password=getpass.getpass('Root Password:'), cmd=install_netperf(), host=None)
    os.system("curl - fsSL https: // get.docker.com - o get - docker.sh")
    os.system("bash get - docker.sh")
    print("Docker Installation is Done")
    sleep(1)


# Pulling Nginx & Centos Images
def Pull():
    print("Starting Pulling Nginx & Centos Images")
    sleep(1)
    os.system("sudo docker pull nginx")
    os.system("sudo docker pull centos")
    print("Nginx & Centos Images We're Pulled Successfully")
    sleep(1)
    os.system("sudo docker images")


# Deploy Images
def Deploy():
    while 1:
        choice = input('''
                        Choose The Image You'd Like To Deploy:
                        1) Deploy Nginx.
                        2) Deploy Centos.
                           ''')
        if choice == "1":
            quan = input("How many Containers Would you like to Deploy")
            for i in quan:
                os.system("sudo docker run -d  `sudo docker images | grep nginx | awk 'NR==1 {print $3}'`")
                print(i, "Done!")
        elif choice == "2":
            quan = input("How many Containers Would you like to Deploy")
            for i in quan:
                os.system("sudo docker run -d  `sudo docker images | grep centos | awk 'NR==1 {print $3}'`")
                print(i, "Done!")
        os.system("sudo docker ps -a")


# Getting Images Info
def info():
    os.system("bash dockerinfo.sh")


# Delete Images
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


# Docker Menu #
def docker_menu():
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


# Python program to validate your IP address

def Check_IP(ip):
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

    while True:
        if re.search(regex, ip):
            print("Your IP address is valid!\n")
            break
        else:
            print("Your IP address is invalid!\n")
            menu()

        # Main Menu"


def menu():
    print("\nHello, welcome to our script :)"
          "\n----------------------------------------")
    ip = input("Please type the desired IP: ")
    Check_IP(ip)
    print("----------------------------------------")
    choose = input("\nPlease choose what you'd like to do: \n"
                   "\n1. Install my key on a remote machine"
                   "\n2. Configure basic installations and packages on my VM"
                   "\n3. Manage AWS machine"
                   "\n4. Install Jenkins master on my VM"
                   "\n5. Install Nagios server"
                   "\n6. Install Netperf tool\n"
                   '\n----------------------------------------'
                   "\nEnter your choice: ")
    if choose == "1":
        ssh_keygen(ip=ip)
    elif choose == "2":
        host = input("Please type the desired hostname: ")
        x = ssh_cmd(ip, user="root", password=getpass.getpass('Root Password:'), cmd=set_install(), host=host)
        f = open('set_install_log.txt', "w")
        f.write(x)
        f.close()
        os.system('touch log.txt; {} >log.txt'.format(x))
        os.system('scp log.txt root@{}:/root/'.format(ip))
    elif choose == "3":
        aws_menu()
    elif choose == "4":
        x = ssh_cmd(ip, user="root", password=getpass.getpass('Root Password:'), cmd=install_jenkins(), host=None)
        f = open('log.txt', "w")
        f.write(x)
        f.close()
        print(x)
    elif choose == "5":
        ssh_cmd(ip, user="root", password=getpass.getpass('Root Password:'), cmd=install_nagios(), host=None)
    elif choose == "5":
        ssh_cmd(ip, user="root", password=getpass.getpass('Root Password:'), cmd=install_netperf(), host=None)
    elif choose == "6":
        docker_menu()

    return


menu()


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
