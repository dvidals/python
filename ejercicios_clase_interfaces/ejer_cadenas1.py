"""Ejercicio 1
Realizar un programa que comprueba si una cadena leída por teclado comienza por una
subcadena introducida por teclado. """
#string[start:stop:step] similar a substring php
#strip(cadena) elimina espacios en blanco
def comienza_por(cadena,subcadena):
    bandera=False
    longitud=len(subcadena)
    for i in range(0,longitud):
        if cadena[i]!=subcadena[i]:
            bandera=True
    if(bandera):
        return cadena+" no comienza por "+subcadena
    else:
         return cadena+" comienza por "+subcadena

a=input("Introduce la cadena con la que quieres trabajar: ")
b=input("Introduce el inicio de la cadena: ")

print(comienza_por(a,b))







