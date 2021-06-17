import queue
# a los constructores por defecto de las colas se le puede pasar como parámetro el tamaño máximo
#para crear una cola de tipo FIFO:
#miCola=queue.Queue() 
#para una cola de tipo LIFO:
#miCola=queue.LifoQueue()
#para una cola de prioridades. Añadimos las prioridades como parámetro.1 es el de mayor prioridad
miCola=queue.PriorityQueue()
miCola.put((3,"Madrid"))
miCola.put((1,"Bogotá"))
miCola.put((2,"México DF"))
print(miCola.get()) #el método get() se utiliza para sacar para información de la cola
print("A continuación se imprimen los elementos restantes en la cola:")
for elemento in miCola.queue:
    print(elemento)
miCola2=queue.Queue(4)
miCola2.put("Madrid")
miCola2.put("Bogotá")
miCola2.put("México DF")
miCola2.put("Lima")
print(miCola2.full())
while not miCola2.empty():
    print(miCola2.get())


