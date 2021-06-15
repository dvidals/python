#Si a un método le pasamos un parámetro precedido de un asterísco estamos indicando un número
#indeterminado de parámetros en una tupla. Si son dos asteríscos, en vez de una tupla sería un diccionario
#Normalmente cuando se trata de una tupla se le denomina *args (lo que en el ejemplo sería *datos)
#Normalmente cuando se trata de un diccionario se le denomina **kwargs(lo que en el ejemplo sería **datos)
class Persona():
    almacen_datos=[]
    def __init__(self,*datos):
        for dato in datos:
            self.almacen_datos.append(dato)
        self.getDatos(self.almacen_datos)
    

    def getDatos(self,info):

        for dato in info:
            print(dato)


        
    
    def __str__(self):
        return "Datos de la persona:\n"\
            +str(self.almacen_datos[0])+"\n"+str(self.almacen_datos[1])+"\n" +str(self.almacen_datos[2])

class Persona2():
    
    lista=[]
    def __init__(self,**datos):
       
        
       elementos=datos.items() #elementos tendríamos una lista de clave y valor
       for clave,valor in elementos:
           
        print(clave, " ", valor)
        self.lista.append(str(clave) + " "+str(valor))
    
            
p1=Persona("David","Vidal",44)
print(p1)
p1.getDatos(p1.almacen_datos)
p2=Persona2(Nombre="Juan", Apellido="Díaz", Edad=18)

for i in range (0, len(p2.lista)):
    print (p2.lista[i])


