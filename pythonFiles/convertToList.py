#from bs4 import BeautifulSoup


#f1 = open("test.html","r") #change to 
f2 = open("LinksFile.txt","w")
newLine = '\n'

with open("backup.txt","r") as f1:
    while True:
        line = f1.readline()
        #if the line has '<li><a href=' then copy it onto the text file
        if '<li><a href=' in line:
            textLine = line.split('"')
            
            f2.write(textLine[1])
            f2.write(newLine)
        if not line:
            break


#f2.write(f1.read())

#open read file
#list = soup.findAll("a",{"target":"blank"})

#print(*list, sep="\n")	#but do this on a file

f1.close()
f2.close()
