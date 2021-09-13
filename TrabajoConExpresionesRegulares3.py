import re
lista_terminos=["camión", "camion", "Camion","niño","niños", "niña","niñas", "ejemplo","Ejemplo"]
lista_abreviaturas=["Ma1","Se1","Ma2","Va1","Ba1","Se2","Ma3","Ma4","Se3","SeA","SeB","Va2","SeC","Ma5","Ma.3","Se:3","Ma:1"]

for termino in lista_terminos:
    if re.findall("^[a-f]", termino) or re.findall("^[A-D]", termino) or re.findall("[s-z]$",termino):
        print(termino)
for abr in lista_abreviaturas:
    if re.findall("Ma[1-3]",abr):
        print(abr)
        
print ("Y ahora al revés, ^ dentro de un rango encuentra los que no están en se rango")
for abr in lista_abreviaturas:
    if re.findall("Ma[^1-3]",abr):
        print(abr)
print ("Otra búsqueda:")
for abr in lista_abreviaturas:
    if re.findall("Se[0-2A-B]",abr):#Encuentra tanto Se1,Se2,SeA,SeB. Es decir, los que están entre 0 y 2, o entre A y B.
        print(abr)
print ("Otra búsqueda:")
for abr in lista_abreviaturas:
    if re.findall("Ma[.:]",abr):
        print(abr)