import xml.etree.ElementTree as etree
from tkinter import *
from tkinter.filedialog import askopenfilename
from Lista_Nombres import Lista
import Generar_grafo
from Lista_Datos import Lista_datos
Lista=Lista()
Lista2=None
Listasuma=Lista_datos()
rut=Tk()
rut.withdraw()
rut.update()
val=None
comparacion0=True
comparacion1=True
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
    contador=0
    for rama in ruta:
        matrizalt=Lista2.Buscar_Nombre(rama.get("nombre"))
        matrizbase=Lista.Buscar_Nombre(rama.get("nombre"))
        Lista1=matrizalt.lista
        Listabase=matrizbase.lista
        for i in range(1,int(matrizalt.filas)+1):
            for j in range(1,int(matrizalt.filas)+1):
                global comparacion1
                comparacion1=True
                for k in range(1,int(matrizalt.columnas)+1):
                    if i!=j:
                        if comparacion1==True:
                            bin1=Lista1.Buscar_binario(i,k)
                            bin2=Listabase.Buscar_binario(j,k)
                            val1=Lista1.Buscar_Dato(i,k)
                            val2=Listabase.Buscar_Dato(j,k)
                            comparacion2=comparacion(bin1,bin2)
                            global comparacion0
                            comparacion0=comparacion1
                            comparacion1=comparacion2
                            if comparacion0==comparacion1:
                                suma=int(val1)+int(val2)
                                global Listasuma
                                Listasuma.Agregar_datos(suma,i,k-1)
                                contador=contador+1
                                print("la Suma es: "+str(suma)+" en la fila: "+str(i)+" y columna: "+str(k))
                            else:
                                while contador!=0:
                                    Listasuma.Eliminar_dato(i)
                                    contador=contador-1
                                    print("Se a eliminado un nodo")
                                comparacion1=False

def lectura(Raiz):
    for rama in Raiz:
        Lista.Agregar_nombre(rama.get("nombre"),rama.get("n"),rama.get("m"),rama)
    global Lista2
    Lista2=Lista

def grafo():
    grafica=input("indique la matriz a graficar")
    if val==1:
        grafic=Lista.Buscar_Nombre(grafica)
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

def main():
    while True:
        opcion=menu()
        if opcion=="1":
            ruta=cargar_archivo()
        if opcion=="2":
            procesar_archivo(ruta)
        if opcion=="4":
            datos_estudiante()
        if opcion=='5':
            grafo()
        if opcion=='6':
            print("Nos vemos pronto")
            break
    return

main()