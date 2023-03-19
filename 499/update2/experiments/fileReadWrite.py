f1 = open("readFile.txt","r")
f2 = open("writeFile.txt","w")

print(f1.read())
f2.write("success")

f1.close()
f2.close()
