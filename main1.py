import statistics
from scipy.stats import sem
import pandas as pd

#para crear una clase
class Medidas:
    #atributos
    perimetros = []
    diametros = []
    nameFile = ""
    nameWorksheet = ""
    decision = ""
    
    #metodos
    def ObtDatos(self):
        #OBTENCION DE DATOS:
        #nombre del archivo para trabajar
        self.nameFile = (input("nombre del archivo: "))+".xlsx"
        #print(self.nameFile)
        #nombre de la hoja para trabajar
        self.nameWorksheet = input("nombre de la hoja a utilizar: ")
        #print(self.nameWorksheet)
        #SE LE PREGUNTA AL USUARIO QUE MEDIDA DESEA UTILIZAR SI PERIMETRO O DIAMETRO
        self.choose()
        #crea una variable donde se lee el archivo indicado y la hoja indicada obteniendo la informacion
        infoArchivo = pd.read_excel(self.nameFile, self.nameWorksheet)
        #cambiar el valor del atributo perimetro de la clase especificada
        self.perimetros = infoArchivo['perimetro'].values.tolist()
        #cambiar el valor del atributo diametro de la clase especificada
        self.diametros = infoArchivo['diametro'].values.tolist() 
        #print (self.diametros)
        
    def choose(self):
        #se ingresa el valor de la decision en un atributo de la clase
        self.decision = input(f'Perimetro(P) o Diametro(D): ')
    def chooser(self):
        #se compara el atributo decision de la clase y si es P entonces perimetro y si es D entonces es diametro
        if (self.decision == "P"):
            return self.perimetros
        elif (self.decision == "D"):
            return self.diametros
    
    def Promedio(self):
        #se hace la operacion para sacar el perimetro
        promedio = statistics.mean(self.chooser())
        #se retorna el promedio
        #return promedio
        #se imprime por consola el promedio
        print(f'El promedio es: {str(promedio)}')
        
    def DesvEstandar(self):
        #se hace la operacion para sacar el perimetro
        desv_stdr = statistics.pstdev(self.chooser())
        #se retorna la desviacion estandar
        #return desv_stdr
        #se imprime por consola la desviacion estandar
        print(f'La desviacion estandar del {self.nameWorksheet} es: {str(desv_stdr)}')
        
    def ErrorEstandar(self):
        #se hace la operacion para obtener el error estandar
        errorStndr = sem(self.chooser())
        #se retorna el valor del mismo
        #return errorStndr
        #se imprime por consola la error estandar
        print(f'El error estandar (error estadistico) del {self.nameWorksheet} es: {str(errorStndr)}')


Circulo1 = Medidas()
Circulo1.ObtDatos()
Circulo1.Promedio()
Circulo1.DesvEstandar()
Circulo1.ErrorEstandar()
