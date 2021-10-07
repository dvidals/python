"""Ejercicio3
Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado."""


def tabla_multiplicar(n):
    print("La tabla del "+str(n)+" es: ")
    for i in range(0,11):
        print(str(n)+"X"+str(i)+"="+str(n*i))
    return ""


try:
    numero=int(input("Introduce el número del que quieras que se muestre la tabla de multiplicar: "))
    
    print(tabla_multiplicar(numero))

except:
        print("No has introducido un número")
   

