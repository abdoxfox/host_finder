import requests
from bs4 import BeautifulSoup

def Get_hosts():
  try:
    user=input('enter your host :> ')
    if user.startswith('http'):
      url= user
    else:
      url = "http://"+user
    page = requests.get(url).content
    page=BeautifulSoup(page, 'html.parser')


    for i in page.findAll('link'):
       if 'http' in i.get('href'):
           
              print(' > ',i.get('href'));print()
    for y in page.findAll('a'):
      try:
       if 'http' in y.get('href'):
           print(' > ',y.get('href'));print()
       elif '//' in y.get('href'):
         print(' > ','https'+y.get('href'));print()
       elif '/' in y.get('href'):
         print(' > ',url+y.get('href'));print()
         
      except:
             break
  except:
    print('  (*_*)    invalid Host  !!!')
def Host_scan():     
  connect_method=input('Enter connection method \nget,post,connect,head....:> ')
  host=input('enter host without "https://" :> ')
  ask_4_proxy=input('do you want to scan with proxy ?? \n[+] if yes enter Y|y\n[+] if no enter N|n\nSo your answer is ?:')
  try:
    r = requests.request(connect_method,'https://'+host)
    if ask_4_proxy.upper()=='Y':
      proxy=input('enter your proxy:port ex 127.0.0.1:8080 :>')
      requests.urllib3.ProxyManager('http://'+proxy)
   
    print('Status code :'+str(r.status_code))
    header=r.headers
    for k,v in header.items():
          print(str(k)+' : ',v)
  except :
   print('''
             (*_*)  invalid host  !!! ''')
def main():
  print("""---------------------Welcome bro------------------------
  List of choices:
  [+] - enter 1 to extract subdomains
  [+] - enter 2 to scan a host
  [+] - enter O to exit
  -----------------------------------------------------------""")
  while True:
    choice=input('enter your choice number :> ')
    if choice =='1':
        Get_hosts()
    if choice =='2':
      Host_scan()
    if choice =='0':
      break
    else:
      pass
if __name__=='__main__':
  main()
