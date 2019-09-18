mystr='welcome to python training'
mystr= mystr.replace(" ","")
x=len(mystr)
statement=(((x/2)%2==0))

if statement:
    value=(x/2)
    print(mystr[value-1])
else:
    value =int(x / 2)+1
    print(mystr[  value])
    print("do something")