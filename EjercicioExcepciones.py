listaNombre=[]
indice=0
print("Crea una lista introduciendo 10 nombres.")

def introduceNombre(valor):
   
    if valor in listaNombre:
        raise ValueError 
    return valor

while(indice<10):
    valor=(str(input("Introduce el nombre "+str(indice+1)+" de 10: ")))
    try: 
        listaNombre.append(introduceNombre(valor))
        indice+=1
    except:
        print("Error.El nombre "+valor+" ya pertence a la lista")
    
print(listaNombre)