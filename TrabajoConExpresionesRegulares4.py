import re

nombre1="Carmen López"
nombre2="Juan Díaz"
nombre3="sandra Martín"
nombre4="Jara Anaya"
nombre5="Lara Montoya"
codigo1="fdsaferfdf255"
codigo2="fdfag255fefafafdf"
codigo3="fafdfadfdsafdffdafaf133fdfdfdfddsfd"

if re.match("Sandra",nombre3,re.IGNORECASE):
    print ("He encontrado a la persona")
else:
    print("No he encontrado a la persona")

if re.match(".ara",nombre4,re.IGNORECASE):
    #el punto "." hace las función de carácter comodín, sustituye a cualquier caracter.
    print ("He encontrado a la persona")
else:
    print("No he encontrado a la persona")

if re.search("255",codigo1):
    print ("He encontrado el código")
else:
    print("No he encontrado el código")

