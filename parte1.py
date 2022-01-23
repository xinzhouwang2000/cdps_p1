from subprocess import call
import os
import sys
import copy

GROUP_NUMBER = ""
if len(sys.argv) > 1:
    GROUP_NUMBER = sys.argv[1]

call("sudo git clone https://github.com/CDPS-ETSIT/practica_creativa2.git", shell = True )
call("sudo apt update", shell = True )
call("sudo apt-get -y install python3-pip", shell = True )
call("sudo pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt", shell = True )
call("sudo cp practica_creativa2/bookinfo/src/productpage/templates/productpage.html practica_creativa2/bookinfo/src/productpage/templates/aux.html", shell = True )

fin = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", 'r') # in file
fout = open("practica_creativa2/bookinfo/src/productpage/templates/aux.html", 'w') # out file
for line in fin:
    if ("Simple Bookstore App" in line) :
        fout.write("{% block title %}Simple Bookstore App "+GROUP_NUMBER+" {% endblock %}")
        fout.write("{% block content %}")  
    else:
        fout.write(line)    
fin.close()
fout.close()
call("sudo mv practica_creativa2/bookinfo/src/productpage/templates/aux.html practica_creativa2/bookinfo/src/productpage/templates/productpage.html", shell = True )
call("sudo rm practica_creativa2/bookinfo/src/productpage/templates/aux.html", shell = True )

call("python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080", shell = True )
