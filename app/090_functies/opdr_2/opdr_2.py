# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(kilometers):
    return kilometers / 1.609344


def miles_naar_kilometers(miles):
    return miles * 1.609344


kilometers = 1223
miles = 867

miles = kilometers_naar_miles(kilometers)
km = miles_naar_kilometers(867)

print(f"{kilometers} kilometers = {miles} miles")
print(f"867 miles = {km} kilometers")