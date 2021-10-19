from datetime import date
 
def getCurrentDate():
    today = date.today()
 
    suffix = "th"
 
    day = today.strftime("%d")
 
    if(day == 1):
        suffix = 'st'
    if(day == 2):
        suffix = 'nd'
    if(day == 3):
        suffix = 'rd'
    else:
        suffix = 'th'
    
    d1 = today.strftime("%d"+suffix+" of %B")
    return d1