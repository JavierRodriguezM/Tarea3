#!/usr/bin/python
from tabulate import tabulate
import time
import argparse

# Función: Recibe un txt y genera otro txt con una tabla que tiene la palabra y el # de veces que se repite
# Entrada: txt
# Salida: txt con tabla que contiene la palabra y el # de veces que esta se repite



# Instrucción para inicializar el parser
parser = argparse.ArgumentParser(description = "Cuenta cada palabra de un archivo de texto y genera otro archivo con una tabla que dice la cantidad de cada palabra")

# Añadir los argumentos que se escribiran en la terminal
parser.add_argument("Archivo", type = str, help= "Nombre del archivo de texto")

# Declaracion de la bandera time.
group = parser.add_mutually_exclusive_group()
group.add_argument("--time", action = "store_true", help = "print time")

# Parseo de los argumentos
args = parser.parse_args()

# Tiempo inicio del método.
tiempo_inicio = time.perf_counter()


def text(file):
    # se abre el archivo como un objeto
    with open(file) as f_obj:
    # se crea una lista donde cada elemento corresponde a cada línea del archivo con \n
        lines = f_obj.readlines()
    # se iniciliza la lista que no tendrá \n
    newlines = []
    # ciclo para ir eliminando \n
    for line in lines:
        line = line.strip("\n")
        newlines.append(line)
    #print(newlines)

    # se inicializa la lista de resultado que no tendrá "_"
    array = []
    # ciclo para recorrer línea por línea
    for line in newlines:
        # se reemplaza los "_" por " "
        line = line.replace("_", " ")
        # se genera una lista de letras
        lista = line.split()
        # ciclo para recorrer palabra por palabra
        for palabra in lista:
            array.append(palabra)
    #print(array)
    # se inicializa la lista para generar tabla
    mydata = []
    # se recorre la lista de todas las palabras
    for palabra in array:
        lista = []
        cont = array.count(palabra)
        # se agrega la palabra
        lista.append(palabra)
        # se agrega la cantidad de veces que aparece
        lista.append(cont)
        # si el la sublista no está, se agrega
        if not(lista in mydata):
            mydata.append(lista)
    #print(mydata)
   
    headers = ["Palabra","# de veces que aparece"]
    tabla = tabulate(mydata, headers=headers)
    print(tabla)
    with open ("file.txt", "w") as f: #Creamos el archivo
        f.write(tabla) #<-Escribimos en el
        f.close()

# Tiempo final del método.        
tiempo_final = time.perf_counter() - tiempo_inicio

def main():
    text(args.Archivo)
    if args.time:
        print("Tiempo ejecución del método=", tiempo_final)
        
# Ejecución del método en la terminal
if __name__ == "__main__":
    main()


