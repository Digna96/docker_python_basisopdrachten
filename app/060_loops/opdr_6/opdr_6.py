# Opdracht 3 input functie
# Naam student:Digna Devilee
# Groep:4ITX7

# Hier komt je code...

# Hier start de for-loop

MyList = ["margharita", "calzone", "verdi", "olivio", "quattro staggioni"]

#sorteer de lijst op alfabetische volgorde
MyList.sort()
print(MyList)

#voeg een pizza toe aan de lijst
MyList.append("hawaii")
print(MyList)

#verwijder de pizza "quattro staggioni" uit de lijst
MyList.remove("quattro staggioni")
print(MyList)   

# print de eerste drie pizza's in de lijst
print(MyList[:3])

#print alleen de middelste pizza in de lijst
print(MyList[2])

#print de laatste drie pizza's in de lijst
print(MyList[-3:])