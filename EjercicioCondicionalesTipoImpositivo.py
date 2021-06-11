renta=float(input("Introduce tu renta en anual: "))
tipo=0
def calcularTipo(renta): 
    if(renta<12000):
     tipo=7
    elif(renta<18000):
        tipo=15
    elif(renta<35000):
        tipo=21
    elif(renta<70000):
        tipo=35
    else:
     tipo=45
    return tipo
print("A la renta "+str(renta)+" le corresponde un "+str(calcularTipo(renta))+"% de tipo impositivo")


