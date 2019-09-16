import pandas as pd

emp_wages={

    "Employee Name":["Rahul","Krish","Shanthan","Ved"],
    "Location":["KPHB","JNTU","Housing Board","Jubilee Hills"],
    "Salary":["1000","5000","2000","70000"]
           }

structured_data=pd.DataFrame(emp_wages)

print(structured_data.loc[structured_data["Salary"]>="5000"])





