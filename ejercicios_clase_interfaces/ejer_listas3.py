"""Ejercicio3
Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa
que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará
cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes
datos:
* Todos los alumnos mayores de edad.
* Los alumnos mayores (los que tienen más edad)
"""

def mayores():
    nombres=[]
    edades=[]
    mayores_de_edad=[]
    mayores_de_todos=[]
    maximo=110
    minimo=0
   
    
    n=input("Introduce el nombre: ")
    edad=input("Introduce la edad: ")

    if(int(edad)>minimo and int(edad)<=maximo):
        #print("Edad en rango")
    

        while n!="*":
            nombres.append(n)
            edades.append(edad)
            n=input("Introduce el nombre: ")
            if n!="*":
                edad=input("Introduce la edad: ")
                if(int(edad)<=minimo and int(edad)>maximo):
                     print ("Edad no válida")
                     break

        
                
        for i in range (0, len(nombres)):
            if int(edades[i])>18:
                mayores_de_edad.append(nombres[i])
            if int(edades[i])>minimo:
                minimo=int(edades[i])

        for i in range (0, len(nombres)):
            if int(edades[i])==minimo:
                mayores_de_todos.append(nombres[i])
    
    else:
        print ("Edad no válida")

   
    
    print(mayores_de_edad) 
    print(mayores_de_todos)         
   
        
mayores()


