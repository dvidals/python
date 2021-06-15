class Persona():
    __nombre=""
    apellido=""
    __edad=0
    genero="sin definir"

    def __init__(self, nombre, apellido,genero):
        self.__nombre=nombre
        self.apellido=apellido
        self.genero=genero

    def setEdad(self,laEdad):
        if laEdad<0 or laEdad>100:
            print("Error en la edad")
        else:
            self.__edad=laEdad
            return self.__edad


    def habla(self):
        return "La persona que se llama " +self.nombre+" está hablando"
    def camina(self):
        return "La persona que se llama "+self.nombre+" está caminando"
    def getDatos(self):
        return "Nombre: "+self.__nombre+" Apellido: "+self.apellido+\
        " Edad: "+str(self.__edad)+" Género: "+self.genero

"""persona1=Persona()
persona1.nombre="Pablo"
persona1.apellido="Vidal"
print(persona1.habla())
print(persona1.getDatos())"""
persona2=Persona("David","Vidal","Masculino")
persona2.setEdad(144)
print(persona2.getDatos())