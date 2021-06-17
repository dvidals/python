from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import time

class PostCrawled():
    def __init__(self,titulo,icono,contenido,imagen):
        self.titulo=titulo
        self.icono=icono
        self.contenido=contenido
        self.imagen=imagen

class PostExtractor():
    def extraeInfo(self):
        urlBase="http://python.beispiel.programmierenlernen.io/index.php"

        # posts=[] Ya no necesito guardarlos en una lista, los quiero uno a uno hasta el 12
        
        while urlBase!="":
           
            time.sleep(2)

            miDoc=requests.get(urlBase)
            docFinal=BeautifulSoup(miDoc.text,"html.parser")
            
            for card in docFinal.select(".card"):
                titulo=card.select(".card-title span")[1].text 
                
                icono=card.select_one(".emoji").text
                contenido=card.select_one(".card-text").text
                imagen=urljoin(urlBase, card.select_one("img").attrs["src"])

                #crawled=PostCrawled(titulo,icono,contenido,imagen) Comentamos esta línea también 
                # porque no queremos que lo almacene en un objeto, queremos que lo devuelva directamente 
                #posts.append(crawled) Comentamos está linea porque no tenemos ya una lista, así que no añadimos nada
                
                yield PostCrawled(titulo,icono, contenido, imagen) #línea nueva
                boton_siguiente=docFinal.select_one(".navigation .btn")
                
            
            if boton_siguiente:
                rutas_absolutas=urljoin(urlBase,boton_siguiente.attrs["href"])
                urlBase=rutas_absolutas
                print(rutas_absolutas)
            else:
                urlBase=""
       # return posts Comentamos está línea porque ya no queremos que nos devuelve una lista, sino de uno en uno
               

losPosts=PostExtractor() 
listaPosts=losPosts.extraeInfo()  #extraeInfo() ya no es un método es un generador.Devuelve un post cada vez que lo llamo


#De la siguiente forma comentada imprimimos los 12 primeros artículos por consola, pero hemos accedido
# a todos, hemos consumido los mismos recursos:

n=1
for elPost in listaPosts:
    if(n<13):
        print(elPost.icono)
        print(elPost.titulo)
        print(elPost.contenido)
        print(elPost.imagen)
        print()
        n=n+1
    else:
        break #para que deje de hacer peticiones al servidor 
    # sin el break ya dejaría de imprimir, pero no de hacer peticiones.




    





