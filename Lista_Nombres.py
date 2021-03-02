from nodo import nodoMatrix
nodo=nodoMatrix

class Lista:
    def __init__(self):
        self.cabeza=None
        self.cola=None

    def vacio(self):
        if self.cabeza== None:
            return True

    def Agregar_nombre(self,nombre,fila,columna,rama):
        nuevo= nodo(nombre,fila,columna,rama)
        if self.vacio()==True:
            self.cabeza=self.cola=nuevo
        else:
            nuevo.next=self.cola
            self.cabeza=nuevo











