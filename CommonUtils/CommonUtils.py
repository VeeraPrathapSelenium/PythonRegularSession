import re
import datetime
def extractPattern_Data(sourcestring,pattern):
    return re.findall(pattern,sourcestring)

def getSystemDateTime():
    print(datetime.datetime.today())
    return datetime.datetime.today()