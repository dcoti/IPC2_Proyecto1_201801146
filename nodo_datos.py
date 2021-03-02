def convertir(nombre):
    if int(nombre)==0:
        return 0
    else:
        return 1

class nodoDatos:
    def __init__(self,nombre,filas,columnas):
        self.nombre=nombre
        self.filas=filas
        self.columnas=columnas
        self.next=None
        binario=convertir(self.nombre)
        #print(self.nombre)
