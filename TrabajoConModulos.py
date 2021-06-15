#import funciones_matematicas
from moduloMatematico.calculosBasicos.funciones_matematicas import sumar,restar,multiplicar,dividir
from moduloMatematico.otrosCalculos.PotenciaYRedondeo import *

#Hay 2 formas de utilizar los módulos:
# 1) antes de la función que queremos usar hay que poner el nombre del módulo cuando importamos el módulo
#2) con from para el módulo y luego import para las funciones que queremos importar
# (se podría usar un asterisco en vez de colocar todas las funciones del módulo que queremos usar).
# En este caso tenemos un paquete, no un modulo. El módulo está en una carpeta distinta a la que nos encontramos
"""funciones_matematicas.sumar(8,2)
funciones_matematicas.restar(8,2)
funciones_matematicas.multiplicar(8,2)
funciones_matematicas.dividir(8,2)"""
sumar(8,2)
restar(8,2)
multiplicar(8,2)
dividir(8,2)
potencia(8,2)
redondear(8.2)