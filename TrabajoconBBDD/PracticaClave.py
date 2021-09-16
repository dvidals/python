import sqlite3
miConexion=sqlite3.connect("TrabajoConBBDD/GestionPedidos")
miCursor=miConexion.cursor()
#Se ponen 3 comillas simples para poder utilizar más de una linea en la instrucción SQL
miCursor.execute(''' 
    CREATE TABLE PRODUCTOS(
        CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
        NOMBRE_ARTICULO VARCHAR(40),
        PRECIO FLOAT,
        SECCION VARCHAR(20)
    )
''')
#si quisieramos un campo que además de campo clave se autoincremental, pondríamos AUTOINCREMENT
misProductos=[("AR01","camiseta",35,"Moda"),("AR02","pantalon",45,"Moda"),("AR03","coche",75,"Jugueteria"),
 ("AR04","gorra",15,"Deportes")   
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)",misProductos)
miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR05','zapatilla',90,'deportes')")
miConexion.commit()
miCursor.close() #para cerrar el cursor y que no quede almacenado en memoria.
miConexion.close()