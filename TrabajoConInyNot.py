trabajadores=["Paula","Manuel","Pedro", "Ana","Sandra"]
lenguajes_Trim1="Java, Python, PHP, C#, HTML, JavaScript"
if "Pedro" in trabajadores:
    print("Sí, Pedro está en la lista")
else: 
    print("Pedro no se ha encontrado en la lista")

if "PHP" in lenguajes_Trim1:
    print("PHP está en el string")
else:
    print("PHP no está")

if "SQL" not in lenguajes_Trim1:
    print("Falta SQL en la lista")
else:
    print("SQL está en la lista")

#otra forma de usar NOT:

if not "SQL" in lenguajes_Trim1:
    print("Falta SQL en la lista")
else:
    print("SQL está en la lista")
