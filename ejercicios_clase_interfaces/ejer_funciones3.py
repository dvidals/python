"""EJERCICIO 3
El día juliano correspondiente a una fecha es un número entero que indica los días que han
transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que
al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las
siguientes subrutinas:
 LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
 DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
 EsBisiesto: Recibe un año y nos dice si es bisiesto.
 Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano."""

def leer_fecha():
    try:
        n1=int(input("Introduce un día del mes: "))
        n2=int(input ("Introduce un mes de en formato numérico, 1 para Enero y 12 para diciembre: "))
        n3=int(input ("Introduce un año: "))

        if n1<1 or n1>31 or n2<1 or n2>13:
            return "La fecha introducida no es correcta"

        elif (n2==11 or n2==4 or n2==6 or n2==9 or n2==2) and n1>30:
            return  "La fecha introducida no es correcta"
    
        elif n2==2 and n1>29:
            return  "La fecha introducida no es correcta"
    
        elif n2==2 and n3%4!=0 and n1>28:
            return "La fecha introducida no es correcta"

        elif n2==2 and (n3%4==0 and n3%100==0 and n3%400!=0) and n1>28:
            return"La fecha introducida no es correcta"
        else:
            #return "La fecha introducida es correcta"
            return n1,n2,n3


    except:
        "Sólo se admiten enteros"
    
    #return n1,n2,n3



def dias_del_mes():
    treinta=[11,4,6,9]
    treinta_y_uno=[1,3,5,7,8,10,12]
    dia,mes,anho=leer_fecha()
    if mes in treinta:
        n1=30
    elif mes in treinta_y_uno:
        n1=31
    elif mes==2:
        if anho%4==0:
            if anho%100==0 and anho%400!=0:
                n1=28
            else:
                n1=29
        else:
            n1=28
    else:
        print("Los meses sólo van del 1 al 12")
        exit()
    print ("Los días de ese mes en ese año son "+ str(n1))
    return n1

def es_bisiesto():
    dia,mes,anho=leer_fecha()
    bandera=True
    if anho%4==0:
         if anho%100==0 and anho%400!=0:
             print ("El año "+str(anho)+" no es bisiesto")
         else:
              print("El año "+str(anho)+" es bisiesto")
              bandera=False
    else:
        print ("El año "+str(anho)+" no es bisiesto")

def calcular_dia_juliano():
    dia,mes,anho=leer_fecha()

   


    