import os #se importa esa clase para poder interactuar con el sistema operativo
import io #para abrir archivos, escribir, etc.
#os.makedirs("NombreDirectorio") crea un directorio con el nombre que le pasemos por parámetro
#os.getcwd() nos indica en que directorio estamos.
#os.chdir("NombreDirectorio") nos mueve al directorio que pasamos por parámetro.
#os.listdir("./") nos muestra todo lo que tenemos en el directorio

#Creamos un directorio y metemos en el un archivo con texto
os.makedirs("PruebaDirectorio") #para crear un directorio
os.chdir("PruebaDirectorio") #para moverse a un directorio
archivo_externo=open("ArchivoEnDirectorio.txt","w+")
archivo_externo.write("Primera frase del archivo creado \nSegunda frase del mismo archivo")
print(os.getcwd())
print(os.listdir("./"))
archivo_externo.seek(0)
print(archivo_externo.read())
archivo_externo.close()