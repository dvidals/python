"""EJERCICIO 2
Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
máximo y el mínimo, utilizando la función anterior.
"""

def calcular_max_min():
    bandera=True
    lista_numeros=[]
    while(bandera):
        try:
            lista_numeros.append(float(input("Introduce un número por teclado: ")))
            bandera2=True
            while bandera2:
                seguir=input("¿Quieres seguir introduciendo números? Si/No :")
                seguir=seguir.lower()
                if(seguir=="no"):
                    bandera=False
                    bandera2=False
                    print(lista_numeros)
                elif seguir=="si":
                    bandera2=False
        except:
            print("Sólo los valores numéricos están permitidos")

    return print("El máximo de los números introducidos es "+ str(max(lista_numeros))+" y el mínimo es "+str(min(lista_numeros)))

calcular_max_min()
        


