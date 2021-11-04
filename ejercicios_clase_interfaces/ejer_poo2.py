"""Ejercicio 2
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona)
y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.
Construye los siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. El atributo cantidad no se puede modificar
directamente, solo ingresando o retirando dinero.
• mostrar(): Muestra los datos de la cuenta.
• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos."""
from ejer_poo1 import persona
class cuenta():

    def __init__(self,titular,cantidad=0,bandera=0):
        self.bandera=bandera #La añado para controlar la ejecución del print. 
        self.titular=titular 
        self.__cantidad=cantidad
        if self.titular.edad<18 and bandera==0:
            self.titular.edad=0
            print("El titular de una cuenta tiene que ser mayor de edad")
        
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self,titular):
        self.__titular=titular

       
    def mostrar(self):
        if self.titular.es_mayor_de_edad():
            return "Cuenta\n"+"Titular:"+self.titular.mostrar()+" - Cantidad:"+str(self.cantidad)
    
    def ingresar(self,ingreso):
        if ingreso > 0:
            self.__cantidad = self.__cantidad + ingreso
    
    def retirar(self,retiro):
        if retiro > 0:
            self.__cantidad = self.__cantidad - retiro
    
"""p1=persona("Katia",19,"36128618B")
print(p1.mostrar())
c1=cuenta(p1,3000)
print(c1.mostrar())
c1.ingresar(300)
print(c1.mostrar())"""


