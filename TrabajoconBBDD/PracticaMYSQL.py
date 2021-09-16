import mysql.connector

miConexion=mysql.connector.connect(host="localhost", database="sql_pildoras", user="root",password="")
miCursor=miConexion.cursor()
miCursor.execute("INSERT INTO EJEMPLO VALUES('36128618B', 'IVAN', 'VIDAL DE SA', 45)")

miCursor.execute("SELECT * FROM PRODUCTOS")

muchosProductos=miCursor.fetchall()

print(muchosProductos)

miConexion.commit()

miCursor.close() #para cerrar el cursor y que no quede almacenado en memoria.

miConexion.close()
