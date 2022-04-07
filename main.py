import sys
sys.path

import statistics
import xlrd
import pandas as pd

infoArchivo = pd.read_excel("doc.xlsx","circulo1")

medsPerimetro = infoArchivo['perimetro'].values.tolist()
count = 0

#while (count < len(medsPerimetro)):
    #print("Perimetro: ", medsPerimetro[count])
    #count = count + 1


#list = [12, 24, 36, 48, 60]
#print("List : " + str(list))
#Promedio de la lista:
promedio = statistics.mean(medsPerimetro)
print("El promedio del perimetro es: " + str(promedio))

#desviacion estandar
desv_stdr = statistics.pstdev(medsPerimetro)
print("La desviacion estandar del promedio es: " + str(desv_stdr))
