# Opdracht 1 functies
# Naam student:
# Groep:

 
def write_to_file(bestandsnaam, oefenen):
    with open(bestandsnaam, "a") as bestand:
        bestand.write(oefenen + "\n")


my_tekst = "Dit is om even te oefenen en om te kijken of het werkt."
my_file = "oefenen.txt"

write_to_file(my_file, my_tekst)