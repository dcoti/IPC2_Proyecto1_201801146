from Lista_Datos import Lista_datos
lista=Lista_datos()

class nodoMatrix:
    def __init__(self,nombre,filas,columnas,rama):
        self.nombre=nombre
        self.filas=filas
        self.columnas=columnas
        self.rama = rama
        self.next=None
        #print(self.nombre)
        for a in rama:
            lista.Agregar_datos(a.text,a.get("x"),a.get("y"))
