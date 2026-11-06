# Opdracht 3 Tekst opslaan
# Naam student: Digna Devilee
# Groep: 4ITX7

tekst = input("Geef de tekst die je wilt encrypten: ")

encrypted = ""

for letter in tekst:
    if letter.isalpha():
        code = ord(letter)
        nieuwe_code = code + 5

        if nieuwe_code > ord('z'):
            nieuwe_code -= 26

        encrypted += chr(nieuwe_code)
    else:
        encrypted += letter

print(encrypted)



