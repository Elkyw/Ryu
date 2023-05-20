#!/usr/bin/python

from socket import *
import random
from termcolor import colored

def scanner(ports):
	global host
	global sock
	sock = socket(AF_INET, SOCK_STREAM)
	sock.settimeout(0.5)
	if (host[:4] == "http"):
		host = sock.gethostbyname(host)
	try:
		sock.connect((host, ports))
		print (colored("[+]port " + str(ports) + " open", 'green'))
	except:
		print (colored("[-]port " + str(ports) + " closed", 'red'))

def banner():
	print ('''                                                                    
\033[1;35m__________________ ____________________________  .___ _______        ____.  _____    
\______   \_____  \ ______   \__    ___/\      \ |   |\      \      |    | /  _  \   
 |     ___//   |   \|       _/ |    |   /   |   \|   |/   |   \     |    |/  /_\  \  
 |    |   /    |    \    |   \ |    |  /    |    \   /    |    \/\__|    /    |    \ 
 |____|   \_______  /____|_  / |____|  \____|__  /___\____|__  /\________\____|__  / 
                  \/       \/                  \/            \/                  \/ ''')


def main():
	global host
	global sock
	host = input("[*] Enter host: ")
	port_range = input("[*] Enter range to scan: ")
	port_range = port_range.split(",")

	for ports in range(int(port_range[0]) , int(port_range[1]) + 1):
		try:
			scanner(ports)
		except:
			sock.close()
			return()

	sock.close()
