from email import header
from bs4 import BeautifulSoup
import requests
import re


f4 = open("ImmigrantLinks.txt","a")

with open("links81.txt","r") as f1:
    while True:
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
        line = f1.readline()
        if not line:
            break
        webSiteName = line[:-1]
        myHumblestOfRequests = requests.get(webSiteName,headers=headers)

        fileText = myHumblestOfRequests.text

        f2 = open("temp.html", "w")
        f2.write(fileText)
        f2.close()
        

        with open("temp.html","r") as f3:
            while True:
                searchLine = f3.readline()
                if 'smuggler' in searchLine:
                    f4.write(line)
                    break
                if 'immigrant'in searchLine:
                    f4.write(line)
                    break
                if 'immigrants' in searchLine:
                    f4.write(line)
                    break
                if 'Mexico' in searchLine:
                    f4.write(line)
                    break
                if 'border'in searchLine:
                    f4.write(line)
                    break
                if 'Border'in searchLine:
                    f4.write(line)
                    break
                if 'migrant' in searchLine:
                    f4.write(line)
                    break
                if 'Mexican' in searchLine:
                    f4.write(line)
                    break
                if 'mexican' in searchLine:
                    f4.write(line)
                    break
                if 'South America' in searchLine:
                    f4.write(line)
                    break
                if 'Patrol' in searchLine:
                    f4.write(line)
                    break
                if 'patrol' in searchLine:
                    f4.write(line)
                    break
                if 'mexico' in searchLine:
                    f4.write(line)
                    break
                if 'undocumented' in searchLine:
                    f4.write(line)
                    break
                if 'crossing' in searchLine:
                    f4.write(line)
                    break
                if 'load' in searchLine:
                    f4.write(line)
                    break
                if 'immigration' in searchLine:
                    f4.write(line)
                    break
                if 'migrants' in searchLine:
                    f4.write(line)
                    break
                if 'ticket' in searchLine:
                    f4.write(line)
                    break
                if 'Spanish' in searchLine:
                    f4.write(line)
                    break
                if 'spanish' in searchLine:
                    f4.write(line)
                    break
                if 'Central America' in searchLine:
                    f4.write(line)
                    break
                if 'birth certificate' in searchLine:
                    f4.write(line)
                    break
                if 'Colombia' in searchLine:
                    f4.write(line)
                    break
                if 'Colombian' in searchLine:
                    f4.write(line)
                    break
                if 'Spain' in searchLine:
                    f4.write(line)
                    break
                if 'Argentina' in searchLine:
                    f4.write(line)
                    break
                if 'Argentinian' in searchLine:
                    f4.write(line)
                    break
                if 'Peru' in searchLine:
                    f4.write(line)
                    break
                if 'Peruvian' in searchLine:
                    f4.write(line)
                    break
                if 'Venezuela' in searchLine:
                    f4.write(line)
                    break
                if 'Venezuelan' in searchLine:
                    f4.write(line)
                    break
                if 'Chile' in searchLine:
                    f4.write(line)
                    break
                if 'Chilean' in searchLine:
                    f4.write(line)
                    break
                if 'Guatemala' in searchLine:
                    f4.write(line)
                    break
                if 'Guatemalan' in searchLine:
                    f4.write(line)
                    break
                if 'Ecuador' in searchLine:
                    f4.write(line)
                    break
                if 'Ecuadorian' in searchLine:
                    f4.write(line)
                    break
                if 'Bolivia' in searchLine:
                    f4.write(line)
                    break
                if 'Bolivian' in searchLine:
                    f4.write(line)
                    break
                if 'Cuba' in searchLine:
                    f4.write(line)
                    break
                if 'Cuban' in searchLine:
                    f4.write(line)
                    break
                if 'Dominican' in searchLine:
                    f4.write(line)
                    break
                if 'Honduras' in searchLine:
                    f4.write(line)
                    break
                if 'Honduran' in searchLine:
                    f4.write(line)
                    break
                if 'Paraguay' in searchLine:
                    f4.write(line)
                    break
                if 'Paraguayan' in searchLine:
                    f4.write(line)
                    break
                if 'El Salvador' in searchLine:
                    f4.write(line)
                    break
                if 'Salvadorean' in searchLine:
                    f4.write(line)
                    break
                if 'Salvadorian' in searchLine:
                    f4.write(line)
                    break
                if 'Nicaragua' in searchLine:
                    f4.write(line)
                    break
                if 'Nicaraguan' in searchLine:
                    f4.write(line)
                    break
                if 'Costa Rica' in searchLine:
                    f4.write(line)
                    break
                if 'Costa Rica' in searchLine:
                    f4.write(line)
                    break
                if 'Panama' in searchLine:
                    f4.write(line)
                    break
                if 'Panamanian' in searchLine:
                    f4.write(line)
                    break
                if 'Uruguay' in searchLine:
                    f4.write(line)
                    break
                if 'Uruguayan' in searchLine:
                    f4.write(line)
                    break
                if 'Equatorial Guinea' in searchLine:
                    f4.write(line)
                    break
                if 'Puertorico' in searchLine:
                    f4.write(line)
                    break
                if 'Puertorican' in searchLine:
                    f4.write(line)
                    break
                if not searchLine:
                    break
        f3.close()
        
f4.close()
f1.close()
