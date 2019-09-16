import re

def extractPattern_Data(sourcestring,pattern):

    return re.findall(pattern,sourcestring)


string='My Pan Number is HJIPM4600E'
ptrn="[A-Z]{5}[0-9]{4}[A-Z]{1}"

print(extractPattern_Data(string,ptrn))







