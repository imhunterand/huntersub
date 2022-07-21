#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests

print ("""                               
┬┌┬┐┬ ┬┬ ┬┌┐┌┌┬┐┌─┐┬─┐┌─┐┌┐┌┌┬┐
││││├─┤│ ││││ │ ├┤ ├┬┘├─┤│││ ││
┴┴ ┴┴ ┴└─┘┘└┘ ┴ └─┘┴└─┴ ┴┘└┘─┴┘
--------------------------@imhunterand------------------------
""")

domain = input("[+] Input domain list : ")
print ("[+] Waiting progress ... \n")

def main(domain):
	url = "https://sonar.omnisint.io/subdomains/{}".format(domain)
	data = requests.get(url).json()
	print ("[+] Olihe kie tok : \n")
	for i in data:
		print(i)
		open('Result.txt','a').write(str(i) + '\n')

if __name__ == '__main__':
	main(domain)
