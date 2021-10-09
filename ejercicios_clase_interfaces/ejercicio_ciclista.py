
def ciclista(h1,segundos):
    hora1=int(h1[0:2])
    minutos1=int(h1[3:5])
    segundos1=int(h1[6:8])
    segundos_totales_iniciales=hora1*3600+minutos1*60+segundos1

    segundos_totales=segundos_totales_iniciales+segundos

    horas=int(segundos_totales/3600)

    horas_float=(segundos_totales/3600)

    

    minutos=int(60*(horas_float-horas))
   

    minutos_float=(60*(horas_float-horas))
    

    segundos=round(60*(minutos_float-minutos))

    
   
    if minutos<10:
        minutos="0"+str(minutos)
    if segundos<10:
        segundos="0"+str(segundos)

    return str(horas)+":"+str(minutos)+":"+str(segundos)
print(ciclista('14:35:50',3600))
print(ciclista('14:35:50',7200))
print(ciclista('14:35:50',1800))
print(ciclista('14:35:50',1820))
print(ciclista('14:35:50',1721))
