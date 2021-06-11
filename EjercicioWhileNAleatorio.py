import random
numero=random.randint(1,100)
numUsuario=int(input("Introduce un número entre 1 y 100: "))
intentos=1
while(numero!=numUsuario):
    if(numero<numUsuario):
        print("El número es menor")
        numUsuario=int(input("Introduce un número menor al que has introducido antes: "))
    else:
        print("El número es mayor")
        numUsuario=int(input("Introduce un número mayor al que has introducido antes: "))
    intentos=intentos+1
print("Correcto. Has utilizado "+str(intentos)+" intentos")