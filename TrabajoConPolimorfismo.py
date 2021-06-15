class Persona():
    def hablar(self):
        return "Hablo como una persona"
class Trabajador(Persona):
    def hablar(self):
        return "Hablo como un trabajador"
class Director(Trabajador):
    def hablar(self):
        return "Hablo como un director"

def hazlesHablar(listaDeLasPersonas):
    for persona in listaDeLasPersonas:
        print(persona.hablar())
def hazlesHablar2(objeto):
    print(objeto.hablar())


Antonio=Persona()
Maria=Trabajador()
Ana=Director()

print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())

print("---------------------------------------------")

listaPersonas=[Antonio,Ana,Maria]
hazlesHablar(listaPersonas)
print("---------------------------------------------")
hazlesHablar2(Maria)
hazlesHablar2(Antonio)
