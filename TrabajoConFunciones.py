def imprimeMensajes():
    print("Este es un curso de Python")
    print("El curso acaba de empezar")
    print("El curos tendrá más de 1500 vídeos")
    print("La anterior línea era broma")
print("El programa ha terminado su ejecución")
def sueldoMes(a,b):
    return a+b

SBase=1000
Comisiones=650
Sueldo=sueldoMes(SBase,Comisiones)
print(Sueldo)

def imprimeMensajes2():

    return "Este es el mensaje de la función"

valorMensaje=imprimeMensajes2()

def imprimeMensajePersonalizado(nombre):
    return "¡Bienvenido "+nombre+"!"

print(imprimeMensajePersonalizado("Carlos"))
