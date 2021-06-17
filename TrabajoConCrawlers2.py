from bs4 import BeautifulSoup
miDoc="""
    <html>
        <body>
            <p>Este es el primer párrafo</p>
            <p>Este es el segundo párrafo</p>
            <a> Es un vínculo</a>

        </body>
    </html>
"""

docFinal=BeautifulSoup(miDoc,"html.parser")
for parrafo in docFinal.find_all("p"):
    print(parrafo.text)
print (docFinal)
print(docFinal.find_all("p"))