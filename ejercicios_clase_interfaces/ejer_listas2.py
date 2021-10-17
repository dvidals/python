"""Ejercicio2
Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas
entre 0 y 10). A continuación, debe mostrar: todas las notas, la nota media, la nota más alta
que ha sacado y la menor.
"""

def lista_notas():
    notas=[]
    suma=0
    max=0
    min=10
    bandera=True
    
    i=0
    for i in range(0,5):
        n=input("Introduce la nota "+str(i+1)+" : ")

        if n.isnumeric():
            notas.append(n)
            suma=suma+float(notas[i])
            if float(notas[i]) > max:
                max=float(notas[i])
            if float(notas[i]) < min:
                min=float(notas[i])
            
        else:
            print ("Las notas tienes que introducirlas como números:")
            bandera=False
            break
    media=suma/len(notas)

    if bandera:
        print("Las notas son las siguientes: ")
        for j in range (0,len(notas)):
            print("Nota "+str(j+1)+": "+notas[j])
        print ("La media es : "+str(media))
        print ("La nota más alta es: "+str(max))
        print ("La nota más baja es: "+str(min))
   
   

lista_notas()

    
    
