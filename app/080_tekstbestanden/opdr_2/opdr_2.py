# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....

import random

geheim_getal = random.randint(1, 100)
aantal_pogingen = 0

while True:
    gok = int(input("Raad mijn geheime getal: "))
    aantal_pogingen += 1
    if gok < geheim_getal:
        print("Hoger!") 
    elif gok > geheim_getal:
        print("Lager!")     
    else: 
        print(f"Gefeliciteerd! Je hebt het geheime getal {geheim_getal} geraden in {aantal_pogingen} pogingen.")
        print(f"Je hebt {aantal_pogingen} pogingen nodig gehad om het getal te raden.")
        break 

