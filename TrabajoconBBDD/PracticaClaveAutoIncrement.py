import sqlite3

miConexion=sqlite3.connect("TrabajoConBBDD/GestionPedidos2")
miCursor=miConexion.cursor()
#Se ponen 3 comillas simples para poder utilizar más de una linea en la instrucción SQL
miCursor.execute(''' 
    CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(40),
        PRECIO FLOAT,
        SECCION VARCHAR(20)
    )
''')
#si quisieramos un campo que además de campo clave se autoincremental, pondríamos AUTOINCREMENT
misProductos=[
    ("camiseta",35,"Moda"),
    ("pantalon",45,"Moda"),
    ("coche",75,"Jugueteria"),
    ("gorra",15,"Deportes")
    
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",misProductos)


miCursor.execute("INSERT INTO PRODUCTOS VALUES(NULL, 'zapatilla',90,'deportes')")

miConexion.commit()

miCursor.close() #para cerrar el cursor y que no quede almacenado en memoria.

miConexion.close()