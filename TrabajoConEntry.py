from tkinter import *
root=Tk()
miFrame=Frame(root,width=1000,height=550)
miFrame.pack()
cuadroNombre=Entry(miFrame)
#cuadroTexto.place(x=120,y=110)
cuadroNombre.grid(row=0,column=1)
cuadroNombre.config(fg="red")
nombreLabel=Label(miFrame,text="Nombre: ")
#nombreLabel.place(x=120,y=110)#Si se colocan en la misma x primero va uno y después del otro
#En vez de usar place podemos usar grid, por ejemplo(comentamos lo anterior). En Grid hay row/column, empiezan en 0.
#El método sticky (n,s,e,w):norte,sur,este y oeste; y sus combinaciones: noroeste, etc.
nombreLabel.grid(row=0,column=0,sticky="w")

apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=1,column=0,sticky="w")
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1)

emailLabel=Label(miFrame,text="Email: ")
emailLabel.grid(row=2,column=0,sticky="w")
cuadroEmail=Entry(miFrame)
cuadroEmail.grid(row=2,column=1,)

direccionLabel=Label(miFrame,text="Dirección del hogar: ")
direccionLabel.grid(row=3,column=0, sticky="w")
cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1)


root.mainloop()