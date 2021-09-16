def funcion_decoradora(funcion_parametro):
    
    def funcion_interna(*args, **kwargs):
        #*args indica que va a recibir un nº indeterminado de parámetros, **kwargs es para pasarle parámetros clave=>valor
        print("A continuación voy a realizar un cálculo")
        funcion_parametro(*args, **kwargs)
        print("Ya he terminado el trabajo")
    return funcion_interna



@funcion_decoradora
def suma(n1,n2,n3):
    print(n1+n2+n3)

@funcion_decoradora
def resta(n1,n2):
    print(n1-n2)

@funcion_decoradora
def potencia(base,exponente):
    print(pow(base,exponente))
    
suma(5,7,35)
resta(20,5)
potencia(5,3)
potencia(base=5,exponente=3) #base es la clave, 5 el valor; lo mismo en el caso del exponente.Fallaría si no pusiésemos **kwargs