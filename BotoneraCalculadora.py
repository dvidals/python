from tkinter import *
#contador=0

def construir_botones(self,botones,filas_botones):
    contador=0
    for fila in range(2,filas_botones+2):
        for columna in range(4):
            botones[contador].grid(row=fila,column=columna)
            contador+=1

#En realidad es crear botón, no colocar_boton. Los botones se colocan con el bucle for anidado:
def colocar_boton(self,valor,mostrar=True, ancho=9, alto=2):
    return Button(self.ventana,text=valor,width=ancho,height=alto,font=("Helvetica",9),
    command=lambda:self.pulsaciones_teclas(valor,mostrar))