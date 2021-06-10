def evaluarAlumno(nota):
    if nota<0 or nota>10:
        valoracion="Nota no permitida"
    
    elif nota<5:
        valoracion="suspenso"
    elif nota<7:
        valoracion="aprobado"
    elif nota<9:
        valoracion="notable"
    else:
         valoracion="sobresaliente"
    return valoracion
notaAlumno=float(input("Introduce la nota: "))
print(evaluarAlumno(notaAlumno))

edad=int(input("Introduce tu edad, por favor: "))
if 18<edad<90:
    print("Puedes intentar obtener el carnet")
else:
    print("Lo siento, no cumples los requisitos")