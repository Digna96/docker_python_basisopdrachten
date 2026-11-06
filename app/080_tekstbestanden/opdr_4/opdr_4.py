# Opdracht 4 Tekst opslaan
# Naam student: Digna Devilee
# Groep:4ITX7


# Party enquete

#maak een list met de volgende vragen: Wat is je voornaam? > 2. Wat is je achternaam? > 3. Wat neem je mee aan drank? > 4. Wat neem je mee om te eten?  

vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

gegevens = {}
for vraag in vragen:
    print(f"{vragen.index(vraag) + 1}. {vraag}")
    antwoord = input()

    if vraag == "Wat is je voornaam?":
        gegevens["voornaam"] = antwoord
    elif vraag == "Wat is je achternaam?":
        gegevens["achternaam"] = antwoord
    elif vraag == "Wat neem je mee aan drank?":
        gegevens["drank"] = antwoord    
    elif vraag == "Wat neem je mee om te eten?":
        gegevens["eten"] = antwoord

print("\nBedankt voor het invullen!")
print("See you at the party.")

with open("party.txt", "a") as bestand:
    for sleutel, waarde in gegevens.items():
        bestand.write(f"{sleutel}: {waarde}\n")

    bestand.write("\n----\n")