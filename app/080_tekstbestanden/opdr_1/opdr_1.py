# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

# Enquete maken

vraag1 = input("Wat vind je van de huidige regering? ")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe? ")
vraag3 = input("Wat vind jij de mooiste stad van Nederland? ")

# Antwoorden opslaan in een tekstbestand
with open("enquete.txt", "w") as bestand:
    bestand.write("Enquete resultaten\n")
    bestand.write(f"Huidige regering: {vraag1}\n")
    bestand.write(f"Python-lessen: {vraag2}\n")
    bestand.write(f"Mooiste stad van Nederland: {vraag3}\n")

print("Bedankt voor het invullen van de enquete!")

