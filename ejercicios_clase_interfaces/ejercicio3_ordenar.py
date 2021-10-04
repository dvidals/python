#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor) 

def ordena(n1,n2,n3):
    if n1>n2 and n1>n3:
        
        return "El número mayor es "+n1
    elif n1>n2 and n1<n3:
        return "El número mayor es "+n3
    elif n1>n2 and n1==n3:
        return "Los números mayores son "+n1+ " y "+n3

    elif n1<n2 and n1<n3:
        if n2>n3:
            return "El número mayor es "+n2

        elif n2<n3:
            return "El número mayor es "+n3
        else: 
            return "Los números mayores son "+n2+" y "+n3
    
    elif n1<n2 and (n1>n3 or n1==n3):

        return "El número mayor es "+n2
    elif n1==n2 and n1==n3:
        return "Los números mayores son "+n1+", "+n2+" y "+n3
    
    elif n1==n2 and n1>n3:

        return "Los números mayores son "+n1+" y "+n2
    elif n1==n2 and n1<n3:

        return "El número mayor es "+n3
    
    
    else:
        return "Ha habido un error"

def ordena2(n1,n2,n3):
    numeros=[n1,n2,n3]
    ordenados=sorted(numeros)
    idx = len(ordenados) - 1
    mayor_menor = []
    while (idx >= 0):
        mayor_menor.append(ordenados[idx])
        idx = idx - 1

    cadena=""
    for numero in mayor_menor:
        cadena=cadena+str(numero)+" "

    return cadena
        
    



numero1=input("Introduce el primer número: ")
numero2=input("Introduce el segundo número: ")
numero3=input("Introduce el tercer número: ")

#print(ordena(numero1,numero2,numero3))
print(ordena2(numero1,numero2,numero3))