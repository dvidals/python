"""Ejercicio 1
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye
los siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
• mostrar(): Muestra los datos de la persona.
• esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
"""

class persona():
    def __init__(self,nombre="",edad=0,dni=""):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    @edad.setter
    def edad(self,edad):
        if edad < 0 or edad > 110:
            print("Edad incorrecta")
            self.__edad=0
        else:
            self.__edad=edad

        
    def validar_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(self.__dni)!=9:
            print("DNI incorrecto")
            self.__dni = ""
        else:
            letra = self.__dni[8]
            num = int(self.__dni[:8])
            if letra.upper() != letras[num % 23]:
                print("DNI incorrecto")
                self.__dni = ""


    @dni.setter
    def dni(self,dni):
        self.__dni=dni
        self.validar_dni()
    
    def mostrar(self):
        return self.nombre+", "+str(self.edad)+" años  y DNI: "+self.dni
    def es_mayor_de_edad(self):
        return self.edad>=18
        """if self.edad>=18:
            return True
        else:
            return False"""
    