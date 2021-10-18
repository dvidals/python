""""Ejercicio 1
Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de
apariciones de cada carácter en la cadena. """


def lee_cadena(cadena):
    diccionario={}
    valores=diccionario.values()
    
    for i in range(len(cadena)):
        if cadena[i] not in diccionario:
            diccionario[cadena[i]]=1
        else:
            diccionario[cadena[i]]=diccionario[cadena[i]]+1
    print (diccionario)

texto=input("Introduce una cadena: ")
texto_minuscula=texto.lower()

lee_cadena(texto_minuscula)
lee_cadena(texto)



