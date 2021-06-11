claves=[]
diccionario={}
def comprobarClave(a,b):
    if a not in b:
        b.append(a)
        diccionario[a]=[]
def comprobarValor(a,b):
    if a not in b:
        b.append(a)
        
    
clave=input("Introduce el país: ")

while(clave!="salir"):    
    comprobarClave(clave,claves)
    valor=input("Introduce ciudad: ")
    comprobarValor(valor,diccionario[clave])
    clave=input("Introduce el país: ")     

print(diccionario)


