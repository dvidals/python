"""Ejercicio4
Diseñar el algoritmo correspondiente a un programa, que:
 Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
 Carga la tabla con valores numéricos enteros.
 Suma todos los elementos de cada fila y todos los elementos de cada columna
visualizando los resultados en pantalla."""

def tabla():
   import random
   suma_fila=[0,0,0,0,0]
   suma_columna=[0,0,0,0,0,]
   lista_tabla=[[0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
   for i in range (0,5):
       for j in range (0,5):
           lista_tabla[i][j]=random.randint(1,100)
   print("La tabla 5x5 con números aletatorios del 1 al 100 que obtenemos es la siguiente: ")        
   print(lista_tabla)

   for i in range (0,5):
       for j in range (0,5):
           suma_fila[i]=suma_fila[i]+lista_tabla[i][j]
           suma_columna[j]=suma_columna[j]+lista_tabla[i][j]
   print("La suma de los elementos de cada una de las filas nos da el siguiente resultado (un valor para la suma de cada fila): ")
   print(suma_fila)
   print("La suma de los elementos de cada una de las columnas nos da el siguiente resultado (un valor para la suma de cada columna): ")
   print(suma_columna)

tabla()