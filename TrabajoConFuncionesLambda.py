def area_tri(b,h):
    area=(b*h)/2
    return area
print (area_tri(3,4))

triangulo2=area_tri(3,6)
triangulo3=area_tri(15,25)

print(triangulo2)
print(triangulo3)

#con funciones lambda 
# (se pone la palabra reservada lambda luego los parámetros y después de los 2 puntos sería lo que devuelve, el return):

area_triangulo=lambda b,h: (b*h)/2
print (area_triangulo(3,6))

potencia_cubo=lambda b:b**3
print (potencia_cubo(3))

formato=lambda comision:"¡"+str(comision)+"!€"
#otra forma:
comision_formato= lambda comision:"¡{}!€".format(comision)

print(formato(25))
print(comision_formato(25))
comision_Antonio=25
print(comision_formato(comision_Antonio))

mi_lista=[5,3,9,15,26,2,39]
mi_lista.sort()
print(mi_lista)
mi_lista.sort(reverse=True)
print(mi_lista)

mi_lista2=[(11,5),(15,7),(2,4),(15,19),(8,4)]
#ordenar los valores de las lista, pero teniendo en cuenta las suma de las tuplas

def ordena_lista(t):
    suma=0
    for i in t:
        suma=suma+i
    #for i in range(0,len(t)):
        #suma=suma+t[i]
    return suma


mi_lista2.sort(key=ordena_lista)
print(mi_lista2)

ordena_lista2=lambda t: t[0]+t[1]

mi_lista2.sort(key=ordena_lista2)
print(mi_lista2)

musicos=["Paul McCartney", "Bruce Springsteen", "Tina Turner", "Justin Bieber", "Elthon John"]

def obtener_apellido(m):
   return m.split(" ")[1]

musicos.sort(key=obtener_apellido)
print(musicos)
        
obtener_apellido2=lambda m:m.split()[1]
musicos.sort(key=obtener_apellido)
print(musicos)

