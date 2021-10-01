def intercambio_variables(a,b):
    c=a
    a="El valor de la variable a es:",b
    b="y el valor de b es:",c
    return a,b

variable1=float(input("Introduce la  variable A:"))
variable2=float(input("Introduce la variable B:"))

print(intercambio_variables(variable1,variable2))