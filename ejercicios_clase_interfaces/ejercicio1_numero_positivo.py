
def numero_positivo(n1):

        if n1>0:
            return "El número es positivo"
        else:
            return "El número es negativo"
try:
    numero=float(input("Introduce un un numero: "))
    print(numero_positivo(numero))
except:
    print("No ha introducido un número")
    



