import datetime
hoy=datetime.date.today()
print(hoy)
print(str(hoy))
print(repr(hoy))#es más preciso que el método __str__. Identifica algo de forma inequívoca (no ambigüa).
#Nos está indicando la clase a la que pertenece el objeto hoy.

class Persona():
    
    def __init__(self,nom, ape, edad):
        self.nombre=nom
        self.apellido=ape
        self.edad=edad
    
    """def __str__(self):
        return "Datos de la persona:\n"+"Nombre: "\
            +self.nombre+"\nApellido: "+self.apellido+"\nEdad: " +str(self.edad)"""
    def __repr__(self):
        return "Datos de la persona:\n"+"Nombre: "\
            +self.nombre+"\nApellido: "+self.apellido+"\nEdad: " +str(self.edad)
class Agenda():
    def __init__(self):
        self.miAgenda={}
    def agregarPersonas(self,nombre,telefono):
        self.miAgenda[nombre]=telefono
    def __len__(self): #sobreescribimos el método len()
        return len(self.miAgenda)
    
p1=Persona("Juan","Díaz", 18)
print(p1)
agenda1=Agenda()
agenda1.agregarPersonas("Juan","464553354")
agenda1.agregarPersonas("María", "986235689")
agenda1.agregarPersonas("Pablo","464553354")
agenda1.agregarPersonas("Paco", "986235689")
agenda1.agregarPersonas("Pedro","464553354")
agenda1.agregarPersonas("Paul", "986235689")
print(len(agenda1))
