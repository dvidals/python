import sqlite3

miConexion=sqlite3.connect("TrabajoConBBDD/miBBDD") #miBBDD es el nombre de la base de datos que voy a crear
#Con la línea anterior abro y creo la conexión. Además he creado una base de datos llamada miBBDD
#Ahora creamos el cursor o puntero:
miCursor=miConexion.cursor()
#Ejecutar query:
#miCursor.execute("create table productos(NARTICULO VARCHAR(50), PRECIO FLOAT, SECCION VARCHAR(20))")
#miCursor.execute("insert into productos values('Camiseta', 25.8,'DEPORTES') ")
muchosProductos=[
    ("Patin",100,"DEPORTES"),
    ("Cenicero",20,"CERAMICA"),
    ("Pantalon",80,"MODA")

]
miCursor.executemany("insert into productos values(?,?,?)", muchosProductos) 
#La anterior es una Consulta paramétrica (?) con 3 parámetros y un iterable (muchosProductos)
#Hay que confirmar la modificaciones que se hagan en las tablas con COMMIT, para crearla no hacía falta:
miConexion.commit()

miCursor.close() #para cerrar el cursor y que no quede almacenado en memoria.

miConexion.close()

