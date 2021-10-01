import math
def ciclista(h1,segundos):
    hora1=int(h1[0:2])
    minutos1=int(h1[3:5])
    segundos1=int(h1[6:8])
    horas=math.ceil(segundos/3600)
    horas_float=(segundos/3600)

    minutos=math.ceil(60*(horas_float-horas))

    minutos_float=(60*(horas_float-horas))

    segundos=math.ceil(60*(minutos_float-minutos))

    horas_finales=hora1+horas
    minutos_finales=minutos+minutos1
    segundos_finales=segundos1+segundos
    if minutos_finales<10:
        minutos_finales="0"+str(minutos_finales)
    if segundos_finales<10:
        segundos_finales="0"+str(segundos_finales)

    return str(horas_finales)+":"+str(minutos_finales)+":"+str(segundos_finales)
print(ciclista('14:35:50',3600))
print(ciclista('14:35:50',7200))
print(ciclista('14:35:50',1800))
print(ciclista('14:35:50',1820))
print(ciclista('14:35:50',1721))
