import sqlite3

miConexion=sqlite3.connect("TrabajoConBBDD/miBBDD") #miBBDD es el nombre de la base de datos que voy a crear
#Con la línea anterior abro y creo la conexión. Además he creado una base de datos llamada miBBDD
#Ahora creamos el cursor o puntero:
miCursor=miConexion.cursor()
#Ejecutar query:
miCursor.execute("select * from productos")

muchosProductos=miCursor.fetchall() #convierte los registros que obtenemos en una lista que se almacena en muchosProductos.
print(muchosProductos)

for i in muchosProductos:
    print("Nombre: ",i[0], " Precio: ",i[1], " Sección: ",i[2])

#Hay que confirmar la modificaciones que se hagan en las tablas con COMMIT, para crearla no hacía falta:
#No se necesita el commit porque no se está modificando la tabla, solo leyéndola

miCursor.close() #para cerrar el cursor y que no quede almacenado en memoria.
miConexion.close()