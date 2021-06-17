from io import open 
archivo_externo=open("segundoArchivo.txt", "w") 
#open crea un archivo externo, parámetros(w,r,a):write,read o append para escribir, leer o modificar.

archivo_externo.write("Primera frase")
archivo_externo.close()#para cerrar el flujo de datos(stream) que habíamos abierto con open.

archivo_externo=open("segundoArchivo.txt", "a") 
archivo_externo.write("\nSegunda frase\nTercera frase")
archivo_externo.close()

archivo_externo=open("segundoArchivo.txt", "r") 
informacion=archivo_externo.read()
archivo_externo.close()
print(informacion)

#Leer línea a línea:
archivo_externo=open("segundoArchivo.txt", "r") 
informacion=archivo_externo.readline()
archivo_externo.close()
print(informacion)

#Leer todas las líneas, devuelve una lista con tantos elementos como líneas haya:
archivo_externo=open("segundoArchivo.txt", "r") 
informacion=archivo_externo.readlines()
archivo_externo.close()
print(informacion)
print(informacion[1])#Para leer una línea en concreto. En este caso, la segunda

