# Opdracht 3 input functie
# Naam student: Digna Devilee
# Groep: 4ITX7

# Hier komt je code...

MyList = []
MyList.append(input("Voeg een kledingstuk toe aan de lijst: "))
MyList.append(input("Voeg nog een kledingstuk toe aan de lijst: "))
MyList.append(input("Voeg nog een kledingstuk toe aan de lijst: "))
MyList.append(input("Voeg nog een kledingstuk toe aan de lijst: "))
MyList.append(input("Voeg nog een kledingstuk toe aan de lijst: "))

MyList.sort(reverse=True)
print(", ".join(MyList))