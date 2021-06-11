import sys
def divide():
    intentos=0
    while True:
        try:
            op1=(float(input("Introduce el primer nº: ")))
            op2=(float(input("Introduce el segundo nº: ")))
            print("El resultado es: "+str(op1/op2))
            break
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
            intentos+=1
            if intentos==3:
                print("Has consumido 3 intentos, el programa finalizará")
                sys.exit()
        except ValueError:
            print("Sólo se aceptan valores numéricos")
            intentos+=1
            if intentos==3:
                print("Has consumido 3 intentos, el programa finalizará")
                sys.exit()
        finally:
            print("Se ha intentado ejecutar la función en su totalidad")

divide()
print("Calculo finalizado. Continuamos con el programa")