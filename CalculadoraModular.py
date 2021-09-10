from tkinter import *
import re

from BotoneraCalculadora import *

raiz=Tk()
class Calculadora:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Calculadora POO")
       #variable en donde se almacenará la operación:
        self.operacion=""
       
        #Agregar displaY:
        
        self.display=Entry(ventana, font="Arial 15")

        #Ubicar display:
        self.display.grid(row=1,column=0,columnspan=4,pady=10)
        self.display.config(background="black",fg="#00db00",justify="right",width=25)

        #Creación de Botones---fila1:
        boton7=colocar_boton(self,7)
        boton8=colocar_boton(self,8)
        boton9=colocar_boton(self,9)
        
        botondiv=colocar_boton(self,u"\u00F7")
        #------------------------------fila 2
        boton4=colocar_boton(self,4)
        boton5=colocar_boton(self,5)
        boton6=colocar_boton(self,6)
        botonx=colocar_boton(self,"x")
        #------------------------------fila 3
        boton1=colocar_boton(self,1)
        boton2=colocar_boton(self,2)
        boton3=colocar_boton(self,3)
        botonres=colocar_boton(self,"-")
        #------------------------------ fila 4
        botoncero=colocar_boton(self,0)
        botoncoma=colocar_boton(self,".")
        botonigual=colocar_boton(self,"=",mostrar=False)
        botonmas=colocar_boton(self,"+")
        #-------------------------------
        
        botones=[boton7,boton8,boton9,botondiv,boton4,boton5,boton6,
        botonx,boton1,boton2,boton3,botonres,botoncero,botoncoma,botonigual,botonmas]

        construir_botones(self,botones,4)

mi_calculadora=Calculadora(raiz)


raiz.mainloop()
        
        
       