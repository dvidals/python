class Vehiculo():
    def __init__(self, Color,Ruedas,Ancho, Alto):
        self.Color=Color
        self.Ruedas=Ruedas
        self.Ancho=Ancho
        self.Alto=Alto
    def Frenar(self):
        return "Estoy frenando"
    
    def Derrapar(self):
        return "Estoy derrapando"
    def Girar(self):
        return "Estoy girando"
    def getDatos(self):
        return "Color: "+self.Color+" Ruedas: "+str(self.Ruedas)+" Ancho: "+str(self.Ancho)+" Alto: " \
        +str(self.Alto)
class Coche (Vehiculo):
    def __init__(self, Color,Ruedas,Ancho, Alto, Cilindrada, Marchas, Asientos=5, Aire_Acondicionado="No"):
        Vehiculo.__init__(self, Color,Ruedas,Ancho, Alto)
        self.Cilindrada=Cilindrada
        self.Marchas=Marchas
        self.Asientos=Asientos
        self.Aire_Acondicionado=Aire_Acondicionado
       
    def Arrancar(self):
        return "Estoy arrancando"
    def Acelerar(self):
        return "Estoy acelerando"
    def Frenar(self):
        return super().Frenar()
    def Derrapar(self):
        return super().Derrapar()
    def Girar(self):
        return super().Girar()
    def Marcha_Atras():
        return "Estoy yendo marcha atrás"
    def getDatos(self):
        return super().getDatos()+" Cilindrada: "+str(self.Cilindrada)+" Marchas: "+str(self.Marchas) \
        +" Asientos: " +str(self.Asientos)+" Aire Acondicionado: "+self.Aire_Acondicionado

class Bicicleta (Vehiculo):
    def __init__(self, Color,Ruedas,Ancho, Alto):
        Vehiculo.__init__(self, Color,Ruedas,Ancho, Alto)
              
    def Saltar(self):
        return "Estoy saltando"
    def Frenar(self):
        return super().Frenar()
    def Derrapar(self):
        return super().Derrapar()
    def Girar(self):
        return super().Girar()
    def getDatos(self):
        return super().getDatos()

class Furgoneta (Coche):
    def __init__(self, Color,Ruedas,Ancho, Alto, Cilindrada, Marchas, Asientos, Aire_Acondicionado):
        Coche.__init__(self, Color,Ruedas,Ancho, Alto,Cilindrada, Marchas, Asientos, Aire_Acondicionado)

    def Cargar(self):
        return "Estoy cargando"
    def Arrancar(self):
        return super().Arrancar()
    def Acelerar(self):
        return super().Acelerar()
    def Frenar(self):
        return super().Frenar()
    def Derrapar(self):
        return super().Derrapar()
    def Girar(self):
        return super().Girar()
    def Marcha_Atras():
        return super().Marcha_Atras()
    def getDatos(self):
        return super().getDatos()

class Moto(Coche,Bicicleta):
    def __init__(self, Color,Ruedas,Ancho, Alto, Cilindrada, Marchas):
        Coche.__init__(self, Color,Ruedas,Ancho, Alto,Cilindrada, Marchas)
    def Arrancar(self):
        return Coche.Arrancar(self)
    def Acelerar(self):
        return Coche.Acelerar(self)
    def Frenar(self):
        return Coche.Frenar(self)
    def Saltar(self):
        return Bicicleta.Saltar(self)
    def Derrapar(self):
        return Coche.Derrapar(self)
    def Girar(self):
        return Coche.Girar(self)
    def getDatos(self):
        return Bicicleta.getDatos(self)+" Cilindrada: "+str(self.Cilindrada)+" Marchas: "+str(self.Marchas)

#Color,Ruedas,Ancho, Alto, Cilindrada, Marchas, Asientos, Aire_Acondicionado
furgoneta1=Furgoneta("Blanco", 5, 1200, 1500, 1900, 5, 5, "NO" )
bicicleta1=Bicicleta("Negro",2,1000,500)
moto1=Moto("Verde",2,1200,1200,650,5)
coche1=Coche("Gris",4,2000,1500,2000,5,5,"Si")

print(furgoneta1.getDatos())
print(bicicleta1.getDatos())
print(moto1.getDatos())
print(coche1.getDatos())
print(furgoneta1.Cargar())
print(bicicleta1.Saltar())
print(coche1.Frenar())
print(moto1.Girar())



    