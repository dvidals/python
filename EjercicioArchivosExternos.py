import os 
import io 
os.chdir("Archivos") 
archivo_externo=open("clientes.txt","r+",encoding='utf-8')#si no podemos el último parámetro nos da error
#print(archivo_externo.read())
archivo_externo.seek(0)
lista_productos=archivo_externo.readlines()
#print(lista_productos)
#print()

archivo_externo.seek(0)
productosNew=[]
for producto in lista_productos:
    campos= producto.split(';')
    cliente="Código Artículo= "+str(campos[0])+" Nombre= "+str(campos[1])+\
    " Dirección= "+str(campos[2])+ " Población= "+str(campos[3])+" Tfno= "+str(campos[4])+\
    " Responsable= "+str(campos[5])
    print(cliente)
    productosNew.append(cliente)
       
#print(productosNew)

