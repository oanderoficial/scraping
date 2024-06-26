import requests 
from bs4 import BeautifulSoup 

pagina = requests.get("https://oander.site")
soup = BeautifulSoup(pagina.text, features="html.parser")

def scraping():
  if pagina.status_code == 200:
    print(pagina.content)
  else:
      print("HTTP error",pagina.status_code)

def text():
   print(soup)

def title():
   print('')
   print(soup.title)
   print('')

def head():
   print('')
   head_ =soup.find('head')
   print(head_)

def meta():
   css_ = soup.find_all('meta')
   print(css_)

def script():
   print ('')
   s =soup.find_all('script')
   print(s)

def links():
   print ('')
   hf = soup.find_all('a')
   print(hf)

while True:
   print ( """

 _       __     __       _____                       _            
| |     / /__  / /_     / ___/______________ _____  (_)___  ____ _
| | /| / / _ \/ __ \    \__ \/ ___/ ___/ __ `/ __ \/ / __ \/ __ `/
| |/ |/ /  __/ /_/ /   ___/ / /__/ /  / /_/ / /_/ / / / / / /_/ / 
|__/|__/\___/_.___/   /____/\___/_/   \__,_/ .___/_/_/ /_/\__, /  
                                          /_/            /____/   
""" )
   print("Scraping oander.site")
   print('')
   print("0 - Testing connection")
   print("1 - Scraping page.txt")
   print("2 - Scraping title")
   print("3 - Scraping <head>")
   print("4 - Scraping <meta>")
   print("5 - Scraping <script>")
   print("6 - Scraping <links>")
   menu = input("Digite uma opção >>>")

   if menu == '1':
      text()
   elif menu == '2':
      title()
   elif menu =='0':
      scraping()
   elif menu =='3':
      head()
   elif menu =='4':
      meta()   
   elif menu =='5':
      script()
   elif menu == '6':
      links()

   else:
      print ("Erro, tente novamente")
