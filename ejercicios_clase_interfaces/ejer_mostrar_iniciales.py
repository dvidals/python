import sys


    
def iniciales(a,b,c):
    
    try:
        for letra in a:
            letra.isalpha() 
           
        for letra in b:
            letra.isalpha() 
           
        for letra in c:
            letra.isalpha() 
            
    except:
        print (" Los números no son carácteres válidos para los datos pedidos")
        sys.exit()
   
    a=a.strip()
    b=b.strip()
    c=c.strip()
    a1=b.find(" ")
    a2=c.find(" ")
    print(a2)
    bandera1=True
    bandera2=True
    if a1>1:
        inicialape=b[a1+1:a1+2]
        bandera1=False
    if a2>1:
        inicialape2=c[a2+1:a2+2]
        bandera2=False

    
    if(bandera1):
        inicial2=b[0:1]
    else:
        inicial2=inicialape
    
    if(bandera2):
        inicial3=c[0:1]
    else:
        inicial3=inicialape2
    
    inicial1=a[0:1]

    print(nombre)
    return inicial1 +", "+ str(inicial2) +", "+ inicial3

nombre=input("Introduce tu nombre: ")
apellido1=input("Introduce tu primer apellido: ")
apellido2=input("Introduce tu segundo apellido: ")

print("Las iniciales son las siguientes: "+iniciales(nombre,apellido1,apellido2))
