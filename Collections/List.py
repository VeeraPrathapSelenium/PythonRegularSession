import re
duplicates=[]
mystr='welcome to python training'
mystr=re.sub("\s*","",mystr)
for x in mystr:
     if mystr.count(x)>1:
         duplicates.append(x)
print(duplicates)




