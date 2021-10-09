"""Ejercicio 4
Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas
se introducen por teclado"""


def encontrar_subcadena(cadena,subcadena):

    if(cadena.find(subcadena)!=-1):
        return "La subcadena se encuentra en la cadena introducida"
    else:
        return "La subcadena NO se encuentra en la cadena introducida"

cadena_input=input("Introduce la cadena con la que quieres trabajar: ").strip()
subcadena_input=input("Introduce la subcadena que quieres saber si está en la cadena que has introducido con anterioridad: ").strip()

print(encontrar_subcadena(cadena_input,subcadena_input))