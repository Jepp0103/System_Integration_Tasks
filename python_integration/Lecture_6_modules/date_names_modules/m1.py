import m2
import m3
import re
 
while (True):
    print("First name:")
    fname = input().strip()
    print("Last name:")
    lname = input().strip()
    if(not re.findall('^[A-Za-zæøåÆØÅ\s-]+$',lname) or not re.findall('^[A-Za-zæøåÆØÅ\s-]+$',fname)):
        print("Invalid input")
    else:
        name = m2.capitalizeNames(fname,lname)
        date = m3.getCurrentDate()
 
        print(f"Hi, today is the {date}. Welcome {name}")