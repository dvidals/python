paises={}
pais=input("Introduce el país: ")
while pais!="salir":
    ciudad=input("Introduce ciudad: ")
    lista_ciudades=paises.setdefault(pais,[ciudad])
    #if lista_ciudades!=[ciudad]:
    if ciudad not in lista_ciudades:
        paises[pais].append(ciudad)
    pais=input("Introduce el país: ")
print(paises)