class Coche():
    ruedas=4
    puertas=5
    largoChasis=260
    anchoChasis=130
    arrancado=False

    def arrancar(self):
        self.arrancado=True

    def estadoCoche(self):
        if(self.arrancado):
            return "El coche está funcionando"
        else:
            return "El coche está parado"

mazda=Coche() #ejemplar de clase
mazda.puertas=3
print(str(mazda.puertas)+" "+str(mazda.largoChasis))
print(mazda.arrancado)
mazda.arrancar()
print(mazda.arrancado)
print(mazda.estadoCoche())