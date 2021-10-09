"""Ejercicio 3
Suponiendo que hemos introducido una cadena por teclado que representa una frase
(palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene. """

def cuenta_palabras(cadena):
    contador=1
    for i in range(0,len(cadena)):
        if cadena[i]==" ":
            contador+=1
    return contador

frase=input("Introduce la cadena con la que quieres trabajar: ")
print("La frase introducida tiene",cuenta_palabras(frase),"palabras")