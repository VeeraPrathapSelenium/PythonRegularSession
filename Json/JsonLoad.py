import json


myfile=open(r"Testdata.json", 'r')


with open(r"Testdata.json", 'r') as myfile:
    if len(myfile.readlines()) != 0:
        myfile.seek(0)
    Bank_0 = json.load(myfile)
    print(Bank_0)