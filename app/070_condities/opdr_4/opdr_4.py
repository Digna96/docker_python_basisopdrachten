# Opdracht 4 condities
# Naam student:
# Groep:




toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

beschikbare_toppings = []

for topping in toppings:
    beschikbare_toppings.append(topping[0])

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} ")

for topping in toppings:
    if keuze == topping[0]:
        print(f"U heeft {keuze} besteld. Dat kost {topping[1]}")
        break
else:
    print("Uw keuze zit niet in ons assortiment")