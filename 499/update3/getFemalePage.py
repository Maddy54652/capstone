from email import header
from bs4 import BeautifulSoup
import requests
import re



#make a thing to get all links

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
#obtain url
URLtoObtain = "https://www.doenetwork.org/uid-geo-us-females.php"

#getting the html
myHumblestOfRequests = requests.get(URLtoObtain,headers = headers)
fileText = myHumblestOfRequests.text

f = open("femalePage.html", "w")
f.write(fileText)
f.close()
