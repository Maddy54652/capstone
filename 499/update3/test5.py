f2 = open("fileTestDoc.txt","a")

with open("test.html","r") as f1:
    while True:
        line = f1.readline()
        #if the line has '<li><a href=' then copy it onto the text file
        if '<li><a href=' in line:
            f2.write(line)
        if not line:
            break

f1.close()
f2.close()
