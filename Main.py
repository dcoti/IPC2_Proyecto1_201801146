import xml.etree.ElementTree as etree
from tkinter import *
from tkinter.filedialog import askopenfilename
from Lista_Nombres import Lista
import Generar_grafo
from Lista_Datos import Lista_datos
Listas=Lista()
Listamatriz=Lista()
Lista2=None
rut=Tk()
rut.withdraw()
rut.update()
val=None
ruta=""

def menu():
    print("Proyecto 1")
    print("-----------------")
    print("1. Cargar archivos")
    print("2. Procesar Archivo")
    print("3. Escribir archivo salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar gráfica")
    print("6. Salir")
    opcion=input("Eliga su opcion: ")
    return opcion

def cargar_archivo():
    file=askopenfilename(filetypes=[("textfile", "*.xml")])
    if file =="":
        print("No selecciono ningun archivo, por favor vuelva a seleccionar")
    else:
        global val
        val = 1
        tree=etree.parse(file)
        Raiz=tree.getroot()
        lectura(Raiz)
        return Raiz

def comparacion(bin1, bin2):
    if bin1==bin2:
        return True
    else:
        return False

def procesar_archivo(ruta):
    print("Calculando la matriz binaria...")
    print("Realizando suma de tuplas...")

    for rama in ruta:
        matrizalt=Lista2.Buscar_Nombre(rama.get("nombre"))
        matrizbase=Listas.Buscar_Nombre(rama.get("nombre"))
        Lista1=matrizalt.lista
        Listabase=matrizbase.lista
        global Listamatriz
        Listamatriz.Agregar_nombre(rama.get("nombre"),0,0,0)
        print(Listamatriz.cabeza.nombre)
        nombre=Listamatriz.Buscar_Nombre(rama.get("nombre"))
        Listasuma = nombre.lista
        for i in range(1,int(matrizalt.filas)+1):
            for j in range(1,int(matrizalt.filas)+1):
                comparacion1=True
                contador = 0
                for k in range(1,int(matrizalt.columnas)+1):

                    if i!=j:
                        if comparacion1==True:
                            bin1=Lista1.Buscar_binario(i,k)
                            bin2=Listabase.Buscar_binario(j,k)
                            val1=Lista1.Buscar_Dato(i,k)
                            val2=Listabase.Buscar_Dato(j,k)
                            comparacion2=comparacion(bin1,bin2)
                            comparacion0=comparacion1
                            comparacion1=comparacion2
                            if comparacion0==comparacion1:
                                suma=int(val1)+int(val2)
                                Listasuma.Agregar_datos(suma,j,k)
                                contador=contador+1
                                print("la Suma es: "+str(suma)+" en la fila: "+str(i)+" y columna: "+str(k))

                            else:
                                while contador!=0:
                                    Listasuma.Eliminar_dato(j,contador)
                                    contador=contador-1
                                    print("Se a eliminado un nodo")
                                comparacion1=False

def lectura(Raiz):
    for rama in Raiz:
        Listas.Agregar_nombre(rama.get("nombre"),rama.get("n"),rama.get("m"),rama)
    global Lista2
    Lista2=Listas

def grafo():
    grafica=input("indique la matriz a graficar")
    if val==1:
        grafic=Listas.Buscar_Nombre(grafica)
        if grafic==0:
            print("No se encontro la matriz")
        else:
            Generar_grafo.Generar(grafic)
            print("Matriz graficada con éxito")
    else:
        print("No se ha cargado ningun archivo")

def datos_estudiante():
    print("Nombre: Daniel Enrique Coti Peñate \nCarne: 201801146\nCurso: Introduccion a la programacion y computacion 2\nSeccion: E"
          "\nEscuela de Ciencias y Sistemas\nCuarto Semestre\n")

def escribir_archivo(ruta):
    data=etree.Element('matrices')
    if Listamatriz.vacio()==True:
        print("Aun no se han procesado datos")
    else:
        for rama in ruta:
            datos= Listamatriz.Buscar_Nombre(rama.get("nombre"))
            base= Listas.Buscar_Nombre(rama.get("nombre"))
            valores=datos.lista
            if valores.cabeza==None:
                valores=base.lista
            matriz=etree.SubElement(data,'matriz')
            matriz.set('name',datos.nombre)
            matriz.set('n',str(datos.filas))
            matriz.set('m',str(datos.columnas))
            for i in range(1,int(rama.get('n'))+1):
                for j in range(1, int(rama.get('m'))+1):
                    value=valores.Buscar_nodo(i,j)
                    if value!=None:
                        valor = etree.SubElement(matriz, 'dato')
                        valor.set('x',str(value.filas))
                        valor.set('y',str(value.columnas))
                        valor.text=str(value.nombre)
        mydata=etree.tostring(data)
        myfile=open('resultado.xml','w')
        myfile.write(str(mydata))
        myfile.close()

def main():
    while True:
        opcion=menu()
        if opcion=="1":
            ruta=cargar_archivo()
        if opcion=="2":
            procesar_archivo(ruta)
        if opcion=="3":
            escribir_archivo(ruta)
        if opcion=="4":
            datos_estudiante()
        if opcion=='5':
            grafo()
        if opcion=='6':
            print("Nos vemos pronto")
            break
    return

main()