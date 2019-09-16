#Step 1
import json

#Step 2
dumpdata={
    "name":"parthap",
    "Age":"29",
    "Place":"Hyderabad",
    "Location":"Kukatpally"
}

#Step 3
jsonfile=open(r"Testdata.json","w")
jsondumpdata=json.dump(dumpdata,jsonfile,ensure_ascii=False,indent=4)
jsonfile.close()


