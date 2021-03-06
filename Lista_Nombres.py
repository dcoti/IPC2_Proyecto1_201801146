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
            self.cabeza=nuevo
        else:
            nuevo.next=self.cabeza
            self.cabeza=nuevo

    def Buscar_Nombre(self,nombre):
        nuevo=self.cabeza
        while (nuevo.nombre!=nombre):
            if nuevo !=None:
                nuevo=nuevo.next
                if nuevo==None:
                    return 0
        return nuevo













