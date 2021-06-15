nUsuario=input("Introduce tu usuario: ")
edad=input("Introduce tu edad, por favor: ")
while(edad.isdigit()==False):
    print("La edad tiene que ser un valor numérico")
    edad=input("Introduce tu edad, por favor: ")

if (int(edad)<18):
    print("No puedes pasar")
else:
    print ("Puedes pasar")

print("El usuario introducido, en mayúsculas,  es: "+nUsuario.upper())
print("El usuario introducido, en minúsculas,  es: "+nUsuario.lower())
print("El usuario introducido, con la primera letra en mayúsculas,  es: "+nUsuario.capitalize())
