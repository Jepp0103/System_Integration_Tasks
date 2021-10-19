def capitalizeNames(name, last_name):
    strip_cap_name = name.strip()
    strip_cap_last_name = last_name.strip()
     
    cap_name = strip_cap_name[0].upper() + strip_cap_name[1:].lower()
    cap_last_name = strip_cap_last_name[0].upper() + strip_cap_last_name[1:].lower()    
    cap_names = cap_name + " " + cap_last_name

    with open("data.db", "w") as db:
        db.write(cap_names)

    return cap_names