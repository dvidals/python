import csv
with open('ejemplo.csv', newline='') as csvfile:
     miCsv = csv.reader(csvfile, delimiter=',')
     for linea in miCsv:
         print(' '.join(linea))