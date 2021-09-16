import psycopg2

miConexion=psycopg2.connect(host="localhost", database="Personas", user="postgres",password="1234")
miCursor=miConexion.cursor()
miCursor.execute("INSERT INTO ALUMNOS VALUES('Pablo', 'López')")

miCursor.execute("SELECT * FROM ALUMNOS")
muchosAlumnos=miCursor.fetchall()
print(muchosAlumnos)

miConexion.commit()

miCursor.close() #para cerrar el cursor y que no quede almacenado en memoria.

miConexion.close()



