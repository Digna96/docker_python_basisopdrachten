# Opdracht 2 lists
# Naam student: Digna Devilee
# Groep:4ITX7


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

print ("rivieren:", rivieren[0])
print (rivier_info[rivieren[0]][1])

print ("rivieren:", rivieren[0].capitalize())
print(rivier_info[rivieren[0]][1].capitalize())

print ("rivieren:", rivieren[1])
print (rivier_info[rivieren[0]][0])

print ("rivieren:", rivieren[1].capitalize())
print (rivier_info[rivieren[0]][0].capitalize())


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())

print("De rivier " + rivieren[0].capitalize() + " stroomt onder andere door " + rivier_info[rivieren[0]][1].capitalize())

print("De rivier " + rivieren[1].capitalize() + " stroomt onder andere door " + rivier_info[rivieren[1]][0].capitalize())

print("De rivier " + rivieren[2].capitalize() + " stroomt onder andere door " + rivier_info[rivieren[2]][2].capitalize())

