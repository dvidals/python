
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import time
import csv

class PostCrawled():
    def __init__(self,titulo,icono,contenido,imagen):
        self.titulo=titulo
        self.icono=icono
        self.contenido=contenido
        self.imagen=imagen

class PostExtractor():
    def extraeInfo(self):
        urlBase="http://python.beispiel.programmierenlernen.io/index.php"
        posts=[]
        #el:
        #while urlBase!="":
        while 1==1:
            #Hacemos un sleep de 2 segundos por cada request para que no se nos deniegue el servicio
            # si realizamos muchas peticiones por segundo. Importamos la clase time para poder usar sleep
            # ahora estamos obteniendo con el bucle while no sólo lo que hay en la página principal, sino
            #que también lo que hay en las demás páginas (en está web tenemos un total de 6 páginas)
            time.sleep(2)

            miDoc=requests.get(urlBase)
            docFinal=BeautifulSoup(miDoc.text,"html.parser")
            
            for card in docFinal.select(".card"):
                titulo=card.select(".card-title span")[1].text 
                #el título está en el segundo span de la clase card-title por eso el [1]
                #se utiliza select_one para coger la primera etiquetas de la coincidencias que nos encontremos 
                """icono=card.select(".emoji")[0].text
                contenido=card.select(".card-text")[0].text
                imagen=card.select("img")[0].attrs["src"]"""

                icono=card.select_one(".emoji").text
                contenido=card.select_one(".card-text").text
                imagen=urljoin(urlBase, card.select_one("img").attrs["src"])

                crawled=PostCrawled(titulo,icono,contenido,imagen)
                posts.append(crawled)
                boton_siguiente=docFinal.select_one(".navigation .btn")
                """
            #el:
            if boton_siguiente:
                rutas_absolutas=urljoin(urlBase,boton_siguiente.attrs["href"])
                urlBase=rutas_absolutas
                print(rutas_absolutas)
            else:
                urlBase=""
        return posts
        #hasta aquí él
        """
            #yo:
            try:
                rutas_absolutas=urljoin(urlBase,docFinal.select_one(".navigation .btn").attrs["href"])
                print(rutas_absolutas)
                urlBase=rutas_absolutas #para que se vaya modificando la página en la que estamos haciendo 
                #el request.Para modificar la ruta absoluta de la pagina que estamos examinando
            except:
                print("No hay más vínculos")
                return posts
                #hasta aquí yo

losPosts=PostExtractor() 
listaPosts=losPosts.extraeInfo()  
#print(listaPosts)

with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    postwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for elPost in listaPosts:
        print(elPost.icono)
        print(elPost.titulo)
        print(elPost.contenido)
        print(elPost.imagen)
        print()
        postwriter.writerow([elPost.icono,elPost.titulo,elPost.contenido,elPost.imagen])


    





