print('devloped by sallami abderrahim ')
print('my nakename ==abdoxfox==')
print('الهوست كيبدا بhttp:// لا تنسى هدا')
from bs4 import BeautifulSoup
 
import requests
def req(url):
	 r=requests.get(url)
	 bs = BeautifulSoup(r.text,"html.parser")
	 try:
	 	for link in bs.findAll('a'):
	 		print(link.get("href"))
	 except SslError:
	 	print('connection to host failed')
	
req(input('enter your host stating with http:// ~: '))