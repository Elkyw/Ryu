#! /usr/bin/python3

from package import port_scanner
from package import subdomain

from termcolor import colored
import os
import sys

__version__ = "1.4.8.8"


def banner():
	print ('''                                                                    
\033[1;31m 

________                
___  __ \____  _____  __
__  /_/ /_  / / /  / / /
_  _, _/_  /_/ // /_/ / 
/_/ |_| _\__, / \__,_/  
        /____/           \033[0m \033[1;35mBy-\033[0m \033[1;36mElkyw@programmer.net\033[0m''')
	print ("version: " + __version__)

def choose():
	print ("\n\n1.Schattenrabe\n2.PortNinja\n3.Exit")
	choice = input()
	if (choice == "1"):
		os.system("cls")
		subdomain.banner()
		subdomain.main()
		choose()
	if (choice == "2"):
		os.system("cls")
		port_scanner.banner()
		port_scanner.main()
		choose()
	if (choice == "3"):
		exit()

os.system("cls")
banner()
help_option = "schattenrabe  -->  Finds subdomain of given domain. It uses a subdomain prefix list located at /usr/local/bin/package/subdomains.txt. You can also append a new prefix to it.\nport scanner  -->  It scans port of given IP address or you can copy paste subdomain name displayed after using RyuKaze."
try:
	if (sys.argv[1] == "-h"):
		print (colored(help_option, 'blue'))
except:
	choose()