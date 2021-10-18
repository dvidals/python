"""Ejercicio 2
Vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa
pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la
fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error.
Tras cada consulta el programa nos preguntará si queremos hacer otra consulta."""

def precio_frutas():
    frutas={'pera':1.99,'manzana':2.55,'naranja':1.69,'mandarina':3.29,'uva':2.56,'ciruela':4.05,'pomelo':3.29}
    bandera=True
    while bandera:
        fruta=input("¿Qué fruta quieres comprar?: ")
        #print(fruta)
        if fruta in frutas:
            try:
                kilos=float(input("¿Cuántos kilos quieres?: "))

                print(frutas[fruta]*kilos)
                seguir=input("¿Quieres hacer otra consulta? Si/No: ")
                seguir=seguir.lower()
                if seguir=="no":
                    bandera=False
                    break
            except:

                print("Tienes que introducir un valor numérico")
        else: 
            print("Esa fruta no la tenemos disponible")
            break


precio_frutas()
    
    