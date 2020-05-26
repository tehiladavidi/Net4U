import sys
import os
import subprocess

def ip():

    return ip


var = input("Please enter the desired IP: ")
command = 'bash /Users/tehilad/set_install.sh {}'.format(var)
os.system(command)
# first = subprocess.Popen(['/bin/echo', var], stdout=subprocess.PIPE)
# second = subprocess.Popen(['bash', '/Users/tehilad/set_install.sh'], stdin=first.stdout)