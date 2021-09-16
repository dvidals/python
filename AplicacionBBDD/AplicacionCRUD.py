from tkinter import *
#para poder trabajar con ventanas emergentes:
from tkinter import messagebox    
import mysql.connector
from mysql.connector.errors import DataError, IntegrityError, NotSupportedError, OperationalError, ProgrammingError

import pymysql
from pymysql.err import MySQLError

root=Tk()

#-----------Conexión/creación BBDD -----------------------------------------------------------

def crearBBDD():
    miConexion=mysql.connector.connect(host="localhost", database="aplicacionpython", user="root",password="")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE  DATOSUSUARIOS(
                ID INT(11) PRIMARY KEY AUTO_INCREMENT,
                NOMBRE VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(100),
                COMENTARIOS VARCHAR(500)
            )
        '''
        )

        messagebox.showinfo("BBDD", "BBDD creada correctamente")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya ha sido creada")

def salir():
    valor_salir=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
    if valor_salir=='yes':
        root.destroy()
    

def borrarCampos():
    cuadroId.delete("0","end")
    nombre.set("") #He mezclado dos formas de hacerlo. Aquí he usado la variable de control nombre(StringVar)
    cuadroContra.delete("0","end")
    cuadroApellido.delete("0","end")
    cuadroDireccion.delete("0","end")
    cuadroComentarios.delete("1.0","end")

'''try:
        miConexion=mysql.connector.connect(host="localhost", database="aplicacionpython", user="root",password="")
        miCursor=miConexion.cursor()
        miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,'" +cuadroNombre.get()+
                        "','" + cuadroContra.get()+
                        "','" + cuadroApellido.get()+
                         "','" + cuadroDireccion.get()+ 
                         "','" + cuadroComentarios.get("1.0",END) + "')")

        
        miConexion.commit()
        messagebox.showinfo("CRUD", "Registro insertado correctamente")'''
def crear():
    try:
        miConexion=mysql.connector.connect(host="localhost", database="aplicacionpython", user="root",password="")
        miCursor=miConexion.cursor()
        miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,'" +cuadroNombre.get()+
                        "','" + cuadroContra.get()+
                        "','" + cuadroApellido.get()+
                         "','" + cuadroDireccion.get()+ 
                         "','" + cuadroComentarios.get("1.0",END) + "')")

        
        miConexion.commit()
        messagebox.showinfo("CRUD", "Registro insertado correctamente")
    except:
        messagebox.showerror("Insertar", "Ha habido un problema")
    
    #con consulta paramétrica, no funcionó
    '''try:
        
        miConexion=pymysql.connect(host="localhost", database="aplicacionpython", user="root",password="")
        miCursor=miConexion.cursor()
        los_datos=(nombre.get(),password.get(),apellido.get(),direccion.get(),cuadroComentarios.get("1.0",END))
        print(los_datos)
        try:
            
            miCursor.execute("INSERT INTO DATOSUSUARIOS(ID,NOMBRE,PASSWORD,APELLIDO,DIRECCION,COMENTARIOS) VALUES (NULL,%s,%s,%s,%s,%s)",(los_datos[0],
            los_datos[1],los_datos[2],los_datos[3],los_datos[4],los_datos[5]))
            miConexion.commit()
            messagebox.showinfo("CRUD", "Registro insertado correctamente")
        except(pymysql.err.OperationalError,pymysql.err.InternalError,pymysql.err.DatabaseError,pymysql.err.DataError,
        pymysql.err.Error) as e:
            print("Ocurrió un error al conectar",e)
            messagebox.showerror("Insertar", "Ha habido un problema SQL")
     
    except:
        messagebox.showerror("Insertar", "Ha habido un problema")'''

        
def actualizar():
    try:
        miConexion=mysql.connector.connect(host="localhost", database="aplicacionpython", user="root",password="")
        miCursor=miConexion.cursor()
        miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE='" +cuadroNombre.get()+
                        "', PASSWORD='" + cuadroContra.get()+
                        "', APELLIDO='" + cuadroApellido.get()+
                         "', DIRECCION='" + cuadroDireccion.get()+ 
                         "',COMENTARIOS='" + cuadroComentarios.get("1.0",END) + "' WHERE ID='"+cuadroId.get()+"'")
        miConexion.commit()
        messagebox.showinfo("CRUD", "Registro actualizado correctamente")
    except:
        messagebox.showerror("Actualizar", "Ha habido un problema")
        
    '''try:#consulta parametrizada solo vale para sqlite
        miConexion=mysql.connector.connect(host="localhost", database="aplicacionpython", user="root",password="")
        miCursor=miConexion.cursor()
        los_datos=cuadroNombre.get(),cuadroContra.get(),cuadroApellido.get(),cuadroDireccion.get(),cuadroComentarios.get("1.0",END)
        print(los_datos)
        miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE=?, PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIOS=? WHERE ID="cuadroId.get(),(los_datos))
        miConexion.commit()
        messagebox.showinfo("CRUD", "Registro actualizado correctamente")
    except:
        messagebox.showerror("Actualizar", "Ha habido un problema")'''

def leer():
    try:
        miConexion=mysql.connector.connect(host="localhost", database="aplicacionpython", user="root",password="")
        miCursor=miConexion.cursor()
        miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID="+cuadroId.get())

        usuario=miCursor.fetchall()
        for i in usuario:
            id.set(i[0])
            nombre.set(i[1])
            password.set(i[2])
            apellido.set(i[3])
            direccion.set(i[4])
            cuadroComentarios.insert(1.0,i[5])

        miConexion.commit()
        messagebox.showinfo("CRUD", "Registro leído correctamente")
    except:
        messagebox.showerror("Leer", "Ha habido un problema")

def borrar():
    try:
        miConexion=mysql.connector.connect(host="localhost", database="aplicacionpython", user="root",password="")
        miCursor=miConexion.cursor()
        miCursor.execute("DELETE  FROM DATOSUSUARIOS WHERE ID="+cuadroId.get())


        miConexion.commit()
        messagebox.showinfo("CRUD", "Registro borrado correctamente")
    except:
        messagebox.showerror("Borrar", "Ha habido un problema")

    
    

#Menu Superior:
#---------------------------------------------------------------------------------------
barraMenu=Menu(root)

root.config(menu=barraMenu, width=300, height=300)

#------------Variables de Control--------------------------

#Opción BBDD:
bbddMenu=Menu(barraMenu, tearoff=0) #tearoff=0 impide que salgan líneas para dividir los elementos
bbddMenu.add_command(label="Crear BBDD", command=crearBBDD)
bbddMenu.add_command(label="Salir", command=salir)

#Opción Borrar:
borrarMenu=Menu(barraMenu, tearoff=0) #tearoff=0 impide que salgan líneas para dividir los elementos
borrarMenu.add_command(label="Borrar campos", command=borrarCampos)

#Opción CRUD:
crudMenu=Menu(barraMenu, tearoff=0) #tearoff=0 impide que salgan líneas para dividir los elementos
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=borrar)

#Opción Ayuda:
ayudaMenu=Menu(barraMenu, tearoff=0) #tearoff=0 impide que salgan líneas para dividir los elementos
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

#Para crear los títulos de las opciones que se desplagarán:
barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

#-------Fin Menú Superior-------------------------------------------------------------------------------------------

#Construcción de campos grid:

#Primer Frame: Frame central:
#----------------------------------------------------------------------------------------------------------------------
miFrame=Frame(root)
miFrame.pack()
#Así lo ha hecho él, pero yo lo he hecho con la función borrar:
id=StringVar()
nombre=StringVar()
password=StringVar()
apellido=StringVar()
direccion=StringVar()


cuadroId=Entry(miFrame,textvariable=id)
#cuadroTexto.place(x=120,y=110)
cuadroId.grid(row=0,column=1, padx=15,pady=15)
cuadroId.config(fg="red")
idLabel=Label(miFrame,text="Id: ")
#idLabel.place(x=120,y=110)#Si se colocan en la misma x primero va uno y después del otro
#En vez de usar place podemos usar grid, por ejemplo(comentamos lo anterior). En Grid hay row/column, empiezan en 0.
#El método sticky (n,s,e,w):norte,sur,este y oeste; y sus combinaciones: noroeste, etc.
idLabel.grid(row=0,column=0,sticky="e")

nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=1,column=0,sticky="e",pady=15)
cuadroNombre=Entry(miFrame,textvariable=nombre)
cuadroNombre.config(fg="red",justify="right")
cuadroNombre.grid(row=1,column=1)

contraLabel=Label(miFrame,text="Password: ")
contraLabel.grid(row=2,column=0,sticky="e",pady=15)
cuadroContra=Entry(miFrame,textvariable=password)
cuadroContra.grid(row=2,column=1)
cuadroContra.config(show="*")


apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=3,column=0,sticky="e",pady=15)
cuadroApellido=Entry(miFrame,textvariable=apellido)
cuadroApellido.grid(row=3,column=1,)

direccionLabel=Label(miFrame,text="Dirección: ")
direccionLabel.grid(row=4,column=0, sticky="e",pady=15)
cuadroDireccion=Entry(miFrame,textvariable=direccion)
cuadroDireccion.grid(row=4,column=1)

#Crearemos una barra de desplazamiento vertical también. Crearemos un objeto scrollbar e indicaremos el elemento padre,etc.
comentariosLabel=Label(miFrame,text="Comentarios: ")
comentariosLabel.grid(row=5,column=0, sticky="e",pady=15)
cuadroComentarios=Text(miFrame,width=16,height=5)
cuadroComentarios.grid(row=5,column=1,padx=15, pady=15)


miScrollVertical=Scrollbar(miFrame, command=cuadroComentarios.yview)
miScrollVertical.grid(row=5,column=2, sticky="nsew")

cuadroComentarios.config(yscrollcommand=miScrollVertical.set)
#-----------Fin del Primer Frame-------------------------------------------

# Segundo Frame, Frame inferior (colocación de botones):

miFrameBotones=Frame(root)
miFrameBotones.pack()

botonCrear=Button(miFrameBotones, text="Crear",command=crear)
botonCrear.grid(row=0,column=0,sticky="e",padx=10,pady=10)

botoLeer=Button(miFrameBotones, text="Leer",command=leer)
botoLeer.grid(row=0,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrameBotones, text="Actualizar",command=actualizar)
botonActualizar.grid(row=0,column=2,sticky="e",padx=10,pady=10)

botonBorrar=Button(miFrameBotones, text="Borrar",command=borrar)
botonBorrar.grid(row=0,column=3,sticky="e",padx=10,pady=10)

#----------Fin del Segundo Frame ----------------------------------------------






#miConexion.commit()

#miCursor.close() #para cerrar el cursor y que no quede almacenado en memoria.

#miConexion.close()

root.mainloop()