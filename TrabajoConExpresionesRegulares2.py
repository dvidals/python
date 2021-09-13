import re
lista_nombres=["Antonio Banderas", "Salma Hayek", "Tomás Cruceros", "Antonio Resines", "Friedrich Hayek"]
lista_terminos=["camión", "camion", "niños", "niñas", "ejemplo"]
for nombre in lista_nombres:
    if re.findall("^Antonio",nombre) or re.findall("Hayek$",nombre):
        #Metacaracteres:^,$, [],
        #los corchetes [] tienen una utilidad parecida a los caracteres comodín: *,? y LIKE de SQL.
        #^ hace referencia al inicio de la cadena. En este casa buscará todos los que empiezan por Antonio.
        #$ hace referencia al final de la cadena
        print(nombre)

for termino in lista_terminos:
    if re.findall("cami[oó]n", termino) or re.findall("niñ[oa]s",termino):
        print(termino)