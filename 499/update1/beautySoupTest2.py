from bs4 import BeautifulSoup
import requests
import re

#helpful link:  https://www.geeksforgeeks.org/beautifulsoup-scraping-link-from-html/
#https://www.w3schools.com/python/python_file_write.asp
#https://proxyway.com/knowledge-base/how-to-find-element-by-id-using-beautifulsoup

#make a thing to get all links


#obtain url
myNameisURL = "https://www.doenetwork.org/uid-geo-us-males.php"

#getting the html
myHumblestOfRequests = requests.get(myNameisURL)
imGonnaGechu = myHumblestOfRequests.text

f = open("test.html", "w")
f.write(imGonnaGechu)
f.close()


#with open(imGonnaGechu) as fp:
#chickenNoodle = BeautifulSoup(myHumblestOfRequests._content,'html.parser')

#zelda = chickenNoodle.find()

print('it worked')
