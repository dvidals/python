import sqlite3

miConexion=sqlite3.connect("TrabajoConBBDD/GestionPedidos2")
miCursor=miConexion.cursor()
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=89.99 WHERE ID=5")
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")

miConexion.commit()

miCursor.close() #para cerrar el cursor y que no quede almacenado en memoria.

miConexion.close()