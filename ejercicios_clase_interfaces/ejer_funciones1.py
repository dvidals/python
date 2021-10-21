"""EJERCICIO 1
Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es
múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el
primero es múltiplo del segundo.
"""

def es_multiplo():
    n1=int(input("Introduce el primer número entero: "))
    n2=int(input("Introduce el segundo número entero: "))

    if(n1%n2==0):
        print (str(n1)+" es múltiplo de "+str(n2))
    else:
         print (str(n1)+" no es múltiplo de "+str(n2))

es_multiplo()