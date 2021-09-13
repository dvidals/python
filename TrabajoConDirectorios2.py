import os 
import io 

"""os.makedirs("PruebaDirectorio2")
os.chdir("PruebaDirectorio2") 
archivo_externo=open("Ejemplo.txt","w+")
archivo_externo.write("Primera frase del archivo creado \nSegunda frase del mismo archivo")
archivo_externo=open("Ejemplo.docx","w+")
archivo_externo.write("Texto de ejemplo ...")
archivo_externo.close()
print(os.getcwd())
print(os.listdir("./"))

#Renombramos el txt con rename pasándole el nombre actual y el que queremos:
#os.rename("Ejemplo.txt","ArchivoAEliminar.txt")
#Para borrarlo, borrar un archivo:
os.remove("ArchivoAEliminar.txt")"""
#Para borrar una carpeta. Por defecto no la deja eliminar si tiene contenido:
#os.rmdir("PruebaDirectorio2") no valdría en este caso.Hay que eliminar el contenido primero
os.chdir("PruebaDirectorio2") 
os.remove("Ejemplo.docx")
os.chdir("..")
os.rmdir("PruebaDirectorio2")
#Para borrar un archivo por el nombre:
listaArchivos=os.listdir("./") #lisdir crea una lista con todos los archivos de ese directorio
for archivo in listaArchivos:
    if archivo=="tirar.py":
        os.remove(archivo)


