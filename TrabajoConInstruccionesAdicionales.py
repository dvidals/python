nombre="Juan Díaz"
#print(len(nombre)) nos daria 9 porque también cuenta el espacio en blanco
contador=0
for i in nombre:
    if(i==" "):
        continue
    contador+=1
print(contador)

#pass se utiliza cuando de momento no se quiere implementar un bucle o una clase, 
# pero para que no de un error. Se coloca el bucle, pero dentro lleva sólo la palabra pass.
#Utilización del else con bucles:
email=input("Introduce tu email, por favor: ")
for i in email:
    if i=="@":
        arroba=True
        break
else:#este arroba está al mismo nivel que el for, no pertenece al if. Sólo entra en el else cuando
    #el bucle se ha ejecutado en su totalidad y no encontrado la arroba.
    arroba=False
print(arroba)
