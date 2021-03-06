import xml.etree.ElementTree as etree
from tkinter import *
from tkinter.filedialog import askopenfilename
from Lista_Nombres import Lista
import Generar_grafo
Lista=Lista()
rut=Tk()
rut.withdraw()
rut.update()
val=None

def menu():
    print("Proyecto 1")
    print("-----------------")
    print("1. Cargar archivos")
    print("2. Procesar Archivo")
    print("3. Escribir archivo salida")
    print("4. Mostrar datos del estudiante")#
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

def procesar_archivo():
    print("")

def lectura(Raiz):
    for rama in Raiz:
        Lista.Agregar_nombre(rama.get("nombre"),rama.get("n"),rama.get("m"),rama)

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

def main():
    while True:
        opcion=menu()
        if opcion=="1":
            cargar_archivo()
        if opcion=='5':
            grafo()
        if opcion=='6':
            print("Nos vemos pronto")
            break
    return

main()