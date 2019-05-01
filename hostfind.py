from bs4 import BeautifulSoup
 
import requests
def req(url):
	 r=requests.get(url)
	 bs = BeautifulSoup(r.text,"html.parser")
	 try:
	 	h=[]
	 	for link in bs.findAll('a'):
	 		host=link.get("href")
	 		h.append(host)
	 	for i in h:
	 		if 'http' in i:
	 			print(i)
	 		
	 except :
	 	print('connection to host failed')

req(input('enter your host stating with http:// ~: '))