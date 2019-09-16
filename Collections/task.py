empdetails={}

print(empdetails)
i=1
while (i<=15):
    empdetails[i] = {"Name":"user"+str(i),
                     "place":"place"+str(i)}
    i+=1
print(empdetails[2])
file =open("mydict.txt","w")
file.write(str(empdetails))
file.close()