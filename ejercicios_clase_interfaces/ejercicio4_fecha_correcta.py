#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta. 





def fecha_correcta(n1,n2,n3):
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
        return "La fecha introducida es correcta"
            

#divisible entre 4
# si además es divisible entre 100 tiene que ser divisible entre 400 para ser bisiesto:

    
    

try:
    numero1=int(input("Introduce el día: "))
    numero2=int(input("Introduce el mes: "))
    numero3=int(input("Introduce el año: "))
    print(fecha_correcta(numero1,numero2,numero3))
   
except:
    print("No has introducido un número")
    

