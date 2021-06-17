from io import open
archivo_externo=open("segundoArchivo.txt","r+")
#print(archivo_externo.read(0))
#para poder volver a leer el documento tenemos que usar seek(), le pasamos por parámetro la posición:
archivo_externo.seek(0)
#print(archivo_externo.read())
archivo_externo.seek(5)
#print(archivo_externo.read())
#read también admite un parámetro,indica el nº de carácteres que va a leer desde donde está el cursor
archivo_externo.seek(0)
mitad=round(len(archivo_externo.read())/2)
archivo_externo.seek(0)

print(archivo_externo.read(mitad))
#lo contrario a lo anterior, la segunda mitad:
archivo_externo.seek(0)
archivo_externo.seek(len(archivo_externo.read())/2)
print(archivo_externo.read())

#ignorar la primera línea:
archivo_externo.seek(0)
archivo_externo.seek(len(archivo_externo.readline()))
print(archivo_externo.read())

#sustituir la segunda línea por otra:
archivo_externo.seek(0)
lista_archivo=archivo_externo.readlines()
lista_archivo[1]="Segunda frase modificada\n"
archivo_externo.seek(0)
"""
for linea in lista_archivo:
    archivo_externo.write(linea)
"""
archivo_externo.writelines(lista_archivo) #las dos anteriores líneas son equivalentes a esta
print(lista_archivo)
archivo_externo.seek(0)
print(archivo_externo.read())


