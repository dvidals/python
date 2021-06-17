def usuarios(usu):
    if  len(usu)<5:
      print("El usuario no puede tener menos de 5 caracteres")
    elif len(usu)>15:
      print ("El usuario no puede tener más de 15 caracteres")
    elif (usu.isalnum()==False):
      print ("El usuario sólo puede contener letras y números")
    else:
      return True


def contrasena(contra):
    if  len(contra)<11:
      print("La contraseña debe tener más de 10 caracteres")
    elif (contra.isalnum()):
        print("La contraseña debe contener un carácter que no sea ni letra ni número")
    
    elif not any(c.isupper() for c in contra) or not any(c.islower() for c in contra):
        print("La contraseña no es segura")
    elif (contra.count(" ")>0):
        print("La contraseña no puede contener espacios en blanco")
    else:
      return True


