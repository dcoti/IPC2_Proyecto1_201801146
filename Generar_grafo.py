
import os

def Generar(lista):
    data=lista.lista
    file=open("Grafo.dot","w")
    file.write("digraph g{\n")
    file.write("filas[label=\""+lista.filas+"\"]\n")
    file.write("columnas[label=\"" + lista.columnas +"\"]\n")
    file.write(lista.nombre+"->filas\n")
    file.write(lista.nombre + "->columnas\n")
    for c in range(1,int(lista.columnas)+1):
        for a in range(1,int(lista.filas)+1):
            data0=data.Buscar_Dato(a,c)
            data_ant=str(a)+str(c)
            file.write(data_ant+"[label=\"" + str(data0) +"\"]\n")
            if a == 1:
                file.write(lista.nombre+"->"+data_ant+"\n")
            else:
                file.write(datai + "->" + data_ant+"\n")
            datai=data_ant

    file.write("}")
    file.close()
    os.system('dot -Tpng Grafo.dot -o Grafo.png')
