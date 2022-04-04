import os
import sys
import halo
import time
import socket
from colorama import Fore
import urllib.request
import socket
import urllib.error
import random
import colorama
import requests
def mrx2():
	idlist = input("List Proxy : ")
	Speed = 1
	def is_bad_proxy(pip): 
		try:
			proxy_handler = urllib.request.ProxyHandler({'http': pip})
			opener = urllib.request.build_opener(proxy_handler)
			opener.addheaders = [('User-agent', 'Mozilla/5.0')]
			urllib.request.install_opener(opener)
			req=urllib.request.Request('http://www.google.com')
			sock=urllib.request.urlopen(req)
		except urllib.error.HTTPError as e:
				g = 0
				return e.code
		except Exception as detail:
				g = 0
				return True
		return False
	def main():
		socket.setdefaulttimeout(Speed)
		proxyList = ""
		for proxyList in open(idlist,'r').read().split("\n"):
			if is_bad_proxy(proxyList):
				print(Fore.RED,(proxyList))
		else:
			print(Fore.GREEN,(proxyList))
			file = open("halogood.txt",'a')
			file.write(proxyList+'\n')
		if __name__ == '__main__':
			main() 
class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
def mrx_pro():
    https = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=no&anonymity=all&simplified=true"
    http = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    socks5 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all"
    socks4 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"
    http_get = requests.get(http).text
    socks4_get = requests.get(socks4).text
    sock5_get = requests.get(socks5).text
    https_get = requests.get(https).text
    print("[1] HTTP [2] HTTPS [3] SOCKS 4 PROXY [4] SOCKS 5 PROXY ")
    ch = input("HALBZHERA ")
    if ch == "1":
        print(colorama.Fore.GREEN+http_get)
        with open('http.txt', 'w') as f:
            f.write(http_get)
            print("Tawaw Save Bu Ba Nawihttp.txt")
    elif ch == "2":
        print(colorama.Fore.GREEN+https_get)
        with open('https.txt', 'w') as f:
            f.write(https_get)
        print("Tawaw Save Bu Banawi https.txt")
    elif ch == "3":
        print(colorama.Fore.GREEN+socks4_get)
        with open('Socks4.txt', 'w') as f:
            f.write(socks4_get)
        print("Tawaw Save Bu Ba Nawi Socks4.txt")
    elif ch == "4":
        print(colorama.Fore.GREEN+sock5_get)
        with open('Socks5.txt', 'w') as f:
            f.write(sock5_get)
        print("Tawaw Save Bu Ba Nawi Socks5.txt")
    else:
        print(colorama.Fore.RED+"FASHALI HENA")
def mrx():
  url=raw_input("linke site babe httt & https:")
  os.system("ping"+' '+url)
def mrx1():
  from datetime import datetime
  now = datetime.now()
  hour = now.hour
  minute = now.minute
  month = now.month
  year = now.year
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  bytes = random._urandom(1490)
  ip =raw_input("IP Target : ")
  port =raw_input("Port       : ")
  print ("[                    ] 0% ")
  time.sleep(4)
  print ("[=====               ] 25%")
  time.sleep(3)
  print ("[==========          ] 50%")
  time.sleep(2)
  print ("[===============     ] 75%")
  time.sleep(1)
  print ("[====================] 100%")
  time.sleep(2)
  sent = 0
  while True:
  	port = port +str(1)
  	sent = sent + 1
  	print ("Sent %s packet to %s port:%s by mrx")%(sent,ip,port)
def mx():
	file1 = open('mx.txt', 'r')
	print(' ')
	print (bcolors.OKGREEN + file1.read() + bcolors.ENDC)
	file1.close()


os.system('clear')
try:
	file1 = open('mx.txt', 'r')
	print(' ')
	print (bcolors.OKGREEN + file1.read() + bcolors.ENDC)
	file1.close()
except IOError:
	print('XWSHKAT DAGEM BATAMY CHET')
print("\033[92m1-url ip")
print("\033[92m2-attack ip")
print("\033[92m3-make proxy")
print("\033[92m4-checkr proxy")
print("\033[92m5-attack website http&https")
kurd =input("\033[92mhalbzhyara:")
if kurd == '1':
	mrx()
if kurd == '2':
	mrx1()
if kurd =='3':
	os.system("clear")
	mx()
	mrx_pro()
if kurd =='4':
	os.system("clear")
	mx()
	mrx2()
if kurd =='5':
	os.system("clear")
	mx()
	mrx=input("linke site : ")
	os.system("python2 att.py"+' '+mrx)
else:
	("tkaya walam rast halbzhyr")
	kurd =input("halbzhyara:")