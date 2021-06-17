from tkinter import *
raiz=Tk() #para crear la raíz, es lo primero que hay que hacer
raiz.title("Tkinter")
raiz.resizable(True,True) #0 o 1, o True/False. La primera es la horizontal y luego la vertical
#el icono tiene que ser .ico y pequeña
raiz.iconbitmap("favicon.ico")
raiz.geometry("700x400")
raiz.config(bg="green")

miFrame=Frame()
miFrame.pack(side="bottom", anchor="w") 
#para empaquetar el Frame dentro de la raíz.El Frame por defecto no tiene tamaño y es transparente
miFrame.config(bg="red")
miFrame.config(width="650", height="350") #El Frame está arriba y centrado, por defecto, dentro de la raíz si no usamos la propiedad side
#cuando lo empaquetamos
#anchor: w(west), e(east), s(south), n(north)
#side: bottom, top, left, right
#fill: x, y, both, none // para rellenar en uno de los ejes o no. El Frame se redimensiones en el eje que le digamos
#expand:0,1 es necesario un 1 para que fill funcione en el eje de las y
miFrame.config(relief="solid") #para darle un borde

raiz.mainloop() #para que la raíz esté siempre ejecutándose 
