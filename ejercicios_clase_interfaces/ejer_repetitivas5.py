"""Ejercicio5
Escribe un programa que diga si un número introducido por teclado es o no primo. Un número
primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente probar hasta la
raíz cuadrada del número para ver si es divisible por algún otro número """

import math;

def primo(n):
    bandera=False
    if n==2: 
        return "El número es primo"
        
    for i in range (2,math.ceil(pow(n,1/2)+1)):
        if(n%i==0):
            bandera=True

    if(bandera):
        return "El número no es primo"
    else:
        return "El número es primo"







numero=int(input("Introduce un número para saber si es primo: "))
    
print(primo(numero))
   

