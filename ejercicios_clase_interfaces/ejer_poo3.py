"""Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuentaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la
cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.
Construye los siguientes métodos para la clase:
• Un constructor.
• Los setters y getters para el nuevo atributo.
• En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por
lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular
es mayor de edad pero menor de 25 años y falso en caso contrario.
• Además la retirada de dinero sólo se podrá hacer si el titular es válido.
• El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de
la cuenta.
Piensa los métodos heredados de la clase madre que hay que reescribir."""

from ejer_poo2 import cuenta
from ejer_poo1 import persona
class cuenta_joven(cuenta):

    def __init__(self,titular,cantidad=0,bonificacion=0):
        super().__init__(titular,cantidad)
        self.bonificacion=bonificacion
        if self.titular.edad<18 or self.titular.edad>=25:
            if self.titular.edad>=25:
                print ("El titular no es válido por no tener una edad inferior a 25 años") 
            else:
                 print ("El titular no es válido") 
            self.titular.nombre=""
            self.titular.edad=0
            self.titular.dni=""
            cuenta.cantidad=0
            self.bonificacion=0
            return
        
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion

    def mostrar(self):
        return "Cuenta Joven\n"+"Titular: "+self.titular.mostrar()+" - Cantidad:"+str(self.cantidad)+ "- Bonificación:"+str(self.bonificacion)+"%"
   
    def es_titular_valido(self):
        return self.titular.edad < 25 and self.titular.es_mayor_de_edad()
    
    def retirar(self,cantidad):
        if not self.es_titular_valido():
            print ("No puesdes retirar el dinero. titular no válido")
        elif cantidad > 0:
            super().retirar(cantidad)

    def ingresar(self,cantidad):
        if not self.es_titular_valido():
            print ("No puesdes ingresar el dinero. titular no válido")
        elif cantidad > 0:
            super().ingresar(cantidad)

print("----------------------------------------------------------")
p1new=persona("David",18,"36128619N")
p2=cuenta(p1new,3000)
p3=cuenta_joven(p1new,p2.cantidad,10)
print(p3.mostrar())

print(p3.cantidad)
print(p3.bonificacion)
print(p3.es_titular_valido())
p3.retirar(400)
print(p3.cantidad)
p3.ingresar(700)
print(p3.cantidad)



print("----------------------------------------------------------")

p1new=persona("David",28,"36128619N")
p2=cuenta(p1new,3000)
p3=cuenta_joven(p1new,p2.cantidad,10)
print(p3.mostrar())

print(p3.cantidad)
print(p3.bonificacion)
print(p3.es_titular_valido())
p3.retirar(400)
print(p3.cantidad)
p3.ingresar(700)
print(p3.cantidad)


print("----------------------------------------------------------")

p1new=persona("David",16,"36128619N")
p2=cuenta(p1new,3000,1) #La añado el 1 (es la bandera) para que no me imprima dos veces la frase "El titular tiene que ser mayor de edad".
p3=cuenta_joven(p1new,p2.cantidad,10)
print(p3.mostrar())




print(p3.cantidad)
print(p3.bonificacion)
print(p3.es_titular_valido())
p3.retirar(400)
print(p3.cantidad)
p3.ingresar(700)
print(p3.cantidad)
