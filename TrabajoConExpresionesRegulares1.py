import re #Hay que importar ese módulo para las expresiones regulares.
cadena="Estoy trabajando con Python en domingo y Semana Santa. El próximo domingo no pienso grabar ningún vídeo"

busqueda="domingo"

texto_encontrado=re.search(busqueda,cadena)


if texto_encontrado is not None: #None es lo que obtendríamos por consola si no lo encuentra.
    print ("Se encontró el término",busqueda+" en la posición " + str(texto_encontrado.start())+ " y termina en la posición "+ 
    str(texto_encontrado.end()))
    print ("Se encontró el término",busqueda+" en la posición " + str(texto_encontrado.span()))
     #span nos devuelve una tupla con el inicio y el final del texto buscado dentro de la cadena.
    listaCoincidencias=re.findall(busqueda,cadena)
    print (re.findall(busqueda,cadena))
    print ("Se ha encontrado la palabra " +busqueda+" en " +str(len(listaCoincidencias))+" ocasiones")

else: 
    print("No se encontró el término ",busqueda)

