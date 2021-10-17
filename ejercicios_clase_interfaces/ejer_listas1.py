"""Ejercicio1
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y
posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su
cubo.
"""

def lista_aletarios():
    import random
    lista=[]
    for i in range(0,10):

        lista.append(random.randint(1,10))
        print("Elemento "+str((i+1))+": "+str(lista[i])+". Cuadrado: "+str(pow(lista[i],2))+". Cubo: "+str(pow(lista[i],3)));

    print (lista)

lista_aletarios();