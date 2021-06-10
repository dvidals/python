lasCapitales={"España":"Madrid", "Francia":"Nantes", "Reino Unido":"Londres",}
lasCapitales["Colombia"]="Bogotá"
lasCapitales["Francia"]="París"
print(lasCapitales)
del lasCapitales["Reino Unido"]
print(lasCapitales)
claveCapitales=["España","Francia","Reino Unido","Colombia","Portugal"]
capitalesMundo={claveCapitales[0]:"Madrid", claveCapitales[1]:"París", claveCapitales[2]:"Londres",
claveCapitales[3]:"Bogotá",claveCapitales[4]:"Lisboa"}
print(capitalesMundo)
print(capitalesMundo["Colombia"])
print(capitalesMundo.keys())
print(capitalesMundo.values())
print(len(capitalesMundo))
# Un diccionario dentro de un diccionario o una lista dentro de un diccionario:
datosJordan={23:"Jordan", "Nombre":"Michael", 
"Equipo":"C. Bulls", "Anillos":[1991,1992,1993,1996,1997,1998], 
"anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(datosJordan.keys())
print(datosJordan["anillos"])
print(datosJordan)