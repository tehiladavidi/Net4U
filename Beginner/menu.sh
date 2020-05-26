echo #!/bin/bash
echo -e "
1.Create files and send them via scp.
2.Check your resources.
3.Retrieve IP address and exchange ssh keys, modify the hostname to net4u.
4.Prepare the enviroment (install required packages)
"
read menu

if [ $menu == "1" ]
then
    echo -e "Please type the name of your folder: "
    read folder
    mkdir /$USER/$folder
    for i in {1..10}
        do
            touch $i.txt
    done
    tar -czvf new.tgz *.txt
    rm *.txt
    du -sh new.tgz
    echo "What is your IP address?"
    read ip
    scp new.tgz root@$ip:/root
    tar -xvf new.tgz
    rm *.txt
    rm *.tgz


elif [ $menu == "2" ]
then
    echo -e "\nYour IP address: "
    ip addr |grep 'enp0s3' |awk 'NR==2 {print $2}'|cut -d"/" -f1
    echo -e "\nYour Disk:"
    df -h | grep /dev/sda1 | awk '{print $2}'
    echo -e "\nYour disk usage: "
    df -h | grep /dev/sda1 | awk '{print $3}'
    echo  -e "Tcp port you're VM is listening to: "
    lsof -i -P -n | grep LISTEN | grep TCP | cut -d"(" -f"1"| awk '{print $9}'
    echo -e "\nOS version: "
    cat /etc/*release | awk 'NR==6 | cut -d "=" -f2
    echo -e "\nKernel version: "
    uname -r
    echo -e "\nCPU version: "
    lscpu | grep "Model name" | cut -d':' -f2
    echo "\nCore number: "
    nproc --all
    echo -e "Total memory: "
    free -m | awk 'NR==2 {print $2}'

elif [ $menu == "3" ]
then
   echo -e "Which IP will be used for the key exchange? "
   read ip
   ssh-copy-id root@$ip
   touch net4u.txt
   echo -e "net4u" >> net4u.txt
   scp net4u.txt root@$ip:/~
   ssh root@$ip << EOF
       cat net4u > /etc/hostname
   EOF

elif [ $menu == "4" ]
then
    echo -e "What is your IP? "
    read ip
    ssh root@$ip << EOF
    apt-get install apache2 -y; \
    apt install apt-transport-https ca-certificates curl software-properties-common; \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -; \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  bionic stable"; \
    apt-get update; \
    apt-cache policy docker-ce; \
    apt-get install docker-ce; \
    apt-get install curl; \
    apt-get install python3.7; \
    apt-get install openjdk-8-jdk -y; \
    apt-get install net-tools -y; \
    wget http://downloads.es.net/pub/iperf/iperf-3.0.6.tar.gz; \
    tar zxvf iperf-3.0.6.tar.gz; \
    cd iperf-3.0.6; \
    ./configure; \
    make; \
    make install; \
    apt-get update; \
    apt install software-properties-common; \
    apt-add-repository --yes --update ppa:ansible/ansible; \
    apt install ansible; \
    update-alternatives --config python
    EOF

fi
