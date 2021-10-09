import sys

def triangulo_rectagulo(a,b):
    c=pow(a*a+b*b,1/2)
    return "La hipotenusa tiene el siguiente resultado: "+str(c)
    
bandera=True
intentos=0
while(bandera):
    if(intentos<3):
        try:
            cateto1=float(input("Introduce el cateto 1:"))
            cateto2=float(input("Introduce el cateto 2:"))
            bandera=False
        except ValueError:
            intentos+=1
            print("Sólo se aceptan valores numéricos")
    else:
        print("Has consumido 3 intentos, deja de hacer el indio... el programa finalizará")
        sys.exit()


#print(triangulo_rectagulo(9,15))
#print(triangulo_rectagulo(3,3))

print(triangulo_rectagulo(cateto1,cateto2))