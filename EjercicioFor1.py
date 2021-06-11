trabajadores=["Marta", "Juana", "Juan", "Elisa", "Pedro"]
trabajadores2=["Juana", "Pedro", "Elisa","Marta", "Juan"]

def comparaLista(a,b):
    bandera=True
    if len(a)!=len(b):
        print("Las listas no tienen ni el mismo número de elementos")
        bandera=False
    else:
        for i in range (0,len(a)):
            if(a[i] not in b):
                bandera=False
    return bandera

if(comparaLista(trabajadores,trabajadores2)):
    print("Las listas son iguales")
else:
    print("Las listas no son idénticas")
    
        
            
