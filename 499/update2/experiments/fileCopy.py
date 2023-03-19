f1 = open("readFile.txt","r")
f2 = open("writeFile.txt","w")

f2.write(f1.read())

f1.close()
f2.close()