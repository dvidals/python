"""Ejercicio1
Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el
producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de
un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120)"""

def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial



try:
    numero=int(input("Introduce el número del que quieras que se calcule el factorial: "))
    
    print(factorial(numero))
   
except:
    print("No has introducido un número")