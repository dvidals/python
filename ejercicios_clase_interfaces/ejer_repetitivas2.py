"""Ejercicio2
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de
todos los números introducidos. """

def suma_y_media(args):
    suma=0
    media=0
    contador=0
    for arg in args:
        contador=contador+1
        suma=suma+arg

    media=suma/(contador-1)


    return "La suma de los números introducidos es " +str(suma)+ " y la media es "+str(media)




lista=[]
bandera=True

while bandera:
    lista.append(int(input("Introduce los números de los que quieras que se calcule la suma y la media.Pulsa cero para salir: ")))
    if lista[-1]==0:
            bandera=False
            

print(suma_y_media(lista))


"""try:

    lista=[]
    bandera=True
    i=0
    while bandera:
        lista[i]=int(input("Introduce los números de los que quieras que se calcule la suma y la media.Pulsa cero para salir "))
        i+=1
        if lista[i]==0:
            bandera=False
            

    print(suma_y_media(lista))
   
except:
    #print("No has introducido un número")"""