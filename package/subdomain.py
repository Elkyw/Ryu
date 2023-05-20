#!/usr/bin/python

import requests
import random
import threading
from termcolor import colored

def request(url):

	try:
		return requests.get("http://" + url, timeout=1)
	except requests.exceptions.ConnectionError:
		pass

def banner():
 print ('''\033[1;35m 
  _________       __            __    __                            ___             
 /   _____/ ____ |  |__ _____ _/  |__/  |_  ____   ________________ \_ |__   ____   
 \_____  \_/ ___\|  |  \__    \   __\   __\/ __ \ /    \_  __ \__  \ | __ \_/ __ \  
 /        \  \___|   Y  \/ __ \|  |  |  | \  ___/|   |  \  | \// __ \| \_\ \  ___/  
/_______  /\___  >___|  (____  /__|  |__|  \___  >___|  /__|  (____  /___  /\___  > 
        \/     \/     \/     \/                \/     \/           \/    \/     \/  ''')

def main():
	target = input("[*] Target Domain: ")

	file = open("package/subdomains.txt", "r")

	for line in file:
		try:
			word = line.strip()
			full_url = word + "." + target
			response = request(full_url)
			if response:
				print (colored("[+] Discovered subdomain: " + full_url, 'green'))
		except:
			return()


