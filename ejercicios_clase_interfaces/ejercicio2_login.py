#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe”
#y “asdasd” se indica “Has entrado al sistema”, sino se da un error 

def login(user,password):
    if user=="pepe" and password=="asdasd":
        return "Has entrado al sistema."
    else:
        return "No existe la pareja usuario/contraseña"

usuario=input("Introduce tu usuario: ")
contrasena=input("Introduce tu contrasena: ")

print(login(usuario,contrasena))
