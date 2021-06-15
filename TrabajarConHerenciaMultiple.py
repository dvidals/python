class Persona():
    def __init__(self, nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def getDatosPersonales(self):
        return "Nombre: "+self.nombre+" Apellido: "+self.apellido+" Edad: "+str(self.edad)
    def habla(self):
        return "Estoy hablando"
    def piensa(self):
        return "Estoy pensando"
    def camina(self):
        return "Estoy caminando"
    def come(self):
        return "Estoy comiendo"

class Estudiante (Persona):
    def __init__(self,nombre, apellido, edad,escuela):
        Persona.__init__(self,nombre,apellido,edad)
        self.escuela=escuela
       

    def estudia(self):
        return "Estoy estudiando"
    
    def getDatosPersonales(self):
        return super().getDatosPersonales()+" Escuela: "+self.escuela
    
class Trabajador(Persona):
    def __init__(self,nombre, apellido, edad,empresa):
       Persona.__init__(self,nombre,apellido,edad)
       self.empresa=empresa
       

    def trabaja(self):
        return "Estoy trabajando"
    
    def getDatosPersonales(self):
        return super().getDatosPersonales()+" Empresa: "+self.empresa

class Director(Trabajador,Estudiante):
    #El orden importa, tiene preferencia en la herencia el trabajador por escribirla primero
    #Tenemos también qe cambiar todas las llamadas a los constructores, también en las anteriores clases,
    # ya no vale utilizar super, hay que utilizar la clase de la que hereda, con el self como primer parámetro
    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):
        Trabajador.__init__(self, nombre, apellido, edad, empresa) 
        Estudiante.__init__(self,nombre, apellido, edad,escuela) 
        self.bonus=bonus

    def dirige(self):
        return "Estoy dirigiendo"
    def getDatosPersonales(self):
        return super().getDatosPersonales()+" Bonus: "+str(self.bonus)


persona1=Persona("Katia","Silva", 41)
estudiante1=Estudiante("David","Vidal",44,"IES Teis")

print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())
print("---------------------------------------------------------------")

trabajador1=Trabajador("David", "Vidal", 44, "C Cope")
print(trabajador1.getDatosPersonales())

director1=Director("Pablo", "Vidal", 10,"Mi Casa", "Coia",3000)
print(director1.getDatosPersonales())
