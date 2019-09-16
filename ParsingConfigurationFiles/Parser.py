import configparser
data=configparser.RawConfigParser()
data.read(r"Environment.cnf")
print(data.get("QA","url"))
print(data.get("QA","username"))
print(data.get("DEV","username"))















