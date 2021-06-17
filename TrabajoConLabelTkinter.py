from tkinter import *

root=Tk()

miFrame=Frame(root, width=700, height=600)
miFrame.pack()

#miLabel=Label(miFrame,text="Hoy es 18 de junio de 2021")
#miLabel.place(x=120, y=125) #si pongo pack() el Frame se adapta al tamaño del Label, no ocupa nada más.
#le estoy indicando que el texto se desplace a esas distancias x,y dentro del Frame.
Label(miFrame,text="Hoy es 18 de junio de 2021",fg="blue",bg="red",font=("Courier",20)).place(x=120,y=325)

miLogo=PhotoImage(file="logo.png")
Label(miFrame,image=miLogo).place(x=120,y=25)
root.mainloop()