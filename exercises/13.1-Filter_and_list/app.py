all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

def starts_with_r(name):
    return name[0].upper() == "R"

resulting_names = list(filter(starts_with_r,all_names))




print(resulting_names)




