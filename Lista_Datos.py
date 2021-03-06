from nodo_datos import nodoDatos
nodo = nodoDatos

class Lista_datos:
    def __init__(self):
        self.cabeza=None
        self.cola=None

    def vacio(self):
        if self.cabeza==None:
            return True

    def Agregar_datos(self,nombre,fila,columna):
        nuevo= nodo(nombre,fila,columna)
        if self.vacio()==True:
            self.cabeza=nuevo
        else:
            nuevo.next=self.cabeza
            self.cabeza=nuevo

    def Buscar_Dato(self,x,y):
        nuevo=self.cabeza
        while nuevo != None:
            if (int(nuevo.filas) == x) & (int(nuevo.columnas) == y):
                return nuevo.nombre
            nuevo=nuevo.next








