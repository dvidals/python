def nota_media(a1,a2,a3,b,c):
    parciales=(a1+a2+a3)/3
    
    calificacion=0.55*parciales+0.30*b+0.15*c
    return calificacion

nota1=float(input("Introduce la nota de tu primer parcial:"))
nota2=float(input("Introduce la nota de tu segundo parcial:"))
nota3=float(input("Introduce la nota de tu tercer parcial:"))
nota_final=float(input("Introduce la nota de tu examen final:"))
trabajo=float(input("Introduce la nota de tu trabajo:"))

print("Nota final: ",nota_media(nota1,nota2,nota3,nota_final,trabajo))
