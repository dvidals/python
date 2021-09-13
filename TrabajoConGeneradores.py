def capitales_mundo(*ciudades): 
#con el asterisco indico que va a recibir un nº indeterminado de ciudades(lo tomará como una tupla)
    for capital in ciudades:
        #yield capital
        #for letra_capital in capital:
            #yield letra_capital 
            yield from capital

#objeto iterable:
capitales_devueltas=capitales_mundo("Berlín", "Roma", "Bogotá", "Pekín", "Hanoi")

print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))

for i in capitales_devueltas:
    print (i)




