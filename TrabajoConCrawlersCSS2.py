from bs4 import BeautifulSoup
import requests

miDoc=requests.get("http://python.beispiel.programmierenlernen.io/index.php")

docFinal=BeautifulSoup(miDoc.text,"html.parser")
iconos=docFinal.select(".emoji")
titulos=docFinal.select("h4 span:nth-child(2n)")
contenidos=docFinal.select(".card p")
imagenes=docFinal.select(".card-block img")

print(iconos[0].text)
print(titulos[0].text)
print(contenidos[0].text)

for parrafo in contenidos:
    print(parrafo.text)
    print("")

for imagen in imagenes:
    print(imagen.attrs["src"])
    


