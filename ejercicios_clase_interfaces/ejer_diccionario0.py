#ejemplo 
diccionario={'one':1,'two':2, 'three':3}
dict1={}
dict1["one"]=1
dict1["two"]=2
len(dict1)
dict1["one"]
del(dict1["one"])
print("two" in dict1)
dicc={'one':1,'two':2, 'three':3}
b=dicc
del(dicc["one"])
#Hay que hacer las copias con el comando copy, si la hacemos así b=dicc al borrar one de dicc también se borra de b. Sucede lo mismo con las listas
dicc={'one':1,'two':2, 'three':3}
b=dicc.copy() #Ya no tendría el problema anterior.
dicc["one"]=10
print(dicc)
print (b)

dicc.clear() #vacío el diccionario.
print(dicc)

#update se utiliza para añadir elementos
b={'four':4}
diccionario.update(b)
print(diccionario)
#get nos devuelve un valor
print(diccionario.get("one"))

#diccionario.pop("one") devuelve el valor y lo elimina
#la función keys() nos va devolviendo las claves
#for clave in dict1.keys():
    #print(clave)
#values() nos va devolviendo los valores
#función items para que devuelva la pareja de clave/valor

#Errores de ejecución: ZeroDivisonError, NameError, TypeError
#Manejo de excepciones, la clausula finally siempre se ejecuta. Importante se pude utilizar también la clausula else como última caso de excepciones:

"""Ejemplo:
while True:
    try:
        x=int(input("Introduce un entero)
    except TypeError:
        print("No se puede convertir a entero)
        """


"""Módulo: Cada uno de los ficheros .py que utilizamos"""