file=open(r"../ResultFolder/abc.txt",'r')
x=file.readline()
while(len(x)>0):
    print(x)
    x=file.readline()
