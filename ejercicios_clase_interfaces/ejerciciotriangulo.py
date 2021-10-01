def triangulo_rectagulo(a,b):
    c=pow(a*a+b*b,1/2)
    return c


cateto1=float(input("Introduce el cateto 1:"))
cateto2=float(input("Introduce el cateto 2:"))

print(triangulo_rectagulo(9,15))
print(triangulo_rectagulo(3,3))

print(triangulo_rectagulo(cateto1,cateto2))