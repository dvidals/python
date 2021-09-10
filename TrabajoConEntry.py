from tkinter import *
from tkinter import messagebox as msg
root=Tk()
miFrame=Frame(root,width=1000,height=550)
miFrame.pack()

nombre=StringVar()
email=StringVar()
direccion=StringVar()
contrasena=StringVar()


cuadroNombre=Entry(miFrame,textvariable=nombre)
#cuadroTexto.place(x=120,y=110)
cuadroNombre.grid(row=0,column=1, padx=15,pady=15)
cuadroNombre.config(fg="red")
nombreLabel=Label(miFrame,text="Nombre: ")
#nombreLabel.place(x=120,y=110)#Si se colocan en la misma x primero va uno y después del otro
#En vez de usar place podemos usar grid, por ejemplo(comentamos lo anterior). En Grid hay row/column, empiezan en 0.
#El método sticky (n,s,e,w):norte,sur,este y oeste; y sus combinaciones: noroeste, etc.
nombreLabel.grid(row=0,column=0,sticky="e")

apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=1,column=0,sticky="e",pady=15)
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1)

contraLabel=Label(miFrame,text="Contraseña: ")
contraLabel.grid(row=2,column=0,sticky="e",pady=15)
cuadroContra=Entry(miFrame,textvariable=contrasena)
cuadroContra.grid(row=2,column=1)
cuadroContra.config(show="*")


emailLabel=Label(miFrame,text="Email: ")
emailLabel.grid(row=3,column=0,sticky="e",pady=15)
cuadroEmail=Entry(miFrame,textvariable=email)
cuadroEmail.grid(row=3,column=1,)

direccionLabel=Label(miFrame,text="Dirección: ")
direccionLabel.grid(row=4,column=0, sticky="e",pady=15)
cuadroDireccion=Entry(miFrame,textvariable=direccion)
cuadroDireccion.grid(row=4,column=1)

#Crearemos una barra de desplazamiento vertical también. Crearemos un objeto scrollbar e indicaremos el elemento padre,etc.
comentariosLabel=Label(miFrame,text="Comentarios: ")
comentariosLabel.grid(row=5,column=0, sticky="e",pady=15)
cuadroComentarios=Text(miFrame,width=15,height=10)
cuadroComentarios.grid(row=5,column=1,padx=15, pady=15)


miScrollVertical=Scrollbar(miFrame, command=cuadroComentarios.yview)
miScrollVertical.grid(row=5,column=2, sticky="nsew")

cuadroComentarios.config(yscrollcommand=miScrollVertical.set)

def funcionBoton():
    #msg.showinfo("Saludo","Hola desde Tkinter")
    #nombre.set("David")
    cuadroComentarios.insert(INSERT,"Hola")
    msg.showinfo("Información rescatada","Nombre: "+nombre.get()+ " Apellido: "+cuadroApellido.get()+" Contraseña: "+contrasena.get()+\
       " Email: "+email.get()+" Dirección: "+direccion.get()+ " Comentarios:" +cuadroComentarios.get(1.0,END))
     

#El botón se podría ubicar en el Frame también, pero habría que indicarle fila y columna, lo ubicaremos en la raíz:
botonEnviar=Button(root,text="Enviar",command=funcionBoton)
botonEnviar.pack()


root.mainloop()