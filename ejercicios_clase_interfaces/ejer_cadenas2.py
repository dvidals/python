"""Ejercicio 2
Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces
aparece el carácter en la cadena. 
"""
def numero_veces(cadena,needle):
    contador=0
    for i in range(0,len(cadena)):
        if cadena[i]==needle:
           contador+=1
    return "El número de veces que aparece "+needle+" en la cadena es "+str(contador)


a=input("Introduce la cadena con la que quieres trabajar: ")

try:
    b=input("Introduce el caracter que quieres buscar: ")
    print(numero_veces(a,b))

except:



