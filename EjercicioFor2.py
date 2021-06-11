n1=int(input("Introduce el primer número: "))
n2=int(input("Introduce el segundo número: "))

for n in range(n1,n2):
    bandera=True
    for i in range(2,n):
        if(n%i==0):
            bandera=False
    if(bandera):
        print(n)
