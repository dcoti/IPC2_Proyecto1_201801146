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

    def Buscar_binario(self, x, y):
        nuevo = self.cabeza
        while nuevo != None:
            if (int(nuevo.filas) == x) & (int(nuevo.columnas) == y):
                return nuevo.binario
            nuevo = nuevo.next

    def Buscar_nodo(self,x,y):
        nuevo=self.cabeza
        while nuevo != None:
            if (int(nuevo.filas) == x) & (int(nuevo.columnas) == y):
                return nuevo
            nuevo=nuevo.next


    def Eliminar_dato(self,i,j):
        anterior=None
        if self.cabeza!=None:
            while self.cabeza!=None:
                if (self.cabeza.filas==i) & (self.cabeza.columnas ==j):
                    if anterior==None:
                        self.cabeza=self.cabeza.next
                    else:
                        anterior.next=self.cabeza.next
                else:
                    anterior=self.cabeza
                    self.cabeza=self.cabeza.next


