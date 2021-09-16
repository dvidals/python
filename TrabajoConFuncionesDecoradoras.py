def funcion_decoradora(funcion_parametro):

    def funcion_interna():
        print("A continuación voy a realizar un cálculo")
        funcion_parametro()
        print("Ya he terminado el trabajo")
    return funcion_interna



@funcion_decoradora
def suma():
    print(25+30)


def resta():
    print(80-25)
    
suma()
resta()