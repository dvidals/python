frases=["Los lunes son los mejores días para programar","Python es moderno", "Veremos inteligencia Artificial más adelante",
"Lambda simplifica el código"];

contar_palabras=lambda f:len(f.split())

frases.sort(key=contar_palabras,reverse=True)
print (frases)
