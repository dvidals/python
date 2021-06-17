sistema_solar="Mercurio Venus Tierra Marte Júpiter Saturno Urano Neptuno Plutón Tierra Mercurio"
"""
planetas=set() #Así se crea un conjunto.
for planeta in sistema_solar.split(" "):
    planetas.add(planeta)
"""
#otra forma:
planetas=set(sistema_solar.split(" "))

print(planetas)
print(len(planetas))