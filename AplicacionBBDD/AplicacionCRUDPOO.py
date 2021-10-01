from tkinter import *
from tkinter import messagebox
import mysql.connector

class crud_poo(Frame):
    def __init__(self,raiz):
        super().__init__(raiz,width=300,height=300) #la clase padre es Frame y le paso la raiz, un ancho y un alto.

root=Tk()
app=crud_poo(root)
app.mainloop()