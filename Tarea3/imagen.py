#!/usr/bin/python
# Librerias para Método img
import cv2
# Otras librerias
import argparse
import time

##########################################################################################################

# Función: Recibe una imagen y despliega otra imagen en pantalla
# Entradas: Nombre de la imagen y escalamiento
# Salida: Imagen escalada

# Instrucción para inicializar el parser
parser = argparse.ArgumentParser(description = "Desplegar imagen en pantalla, de acuerdo a una escala elegida")

# Añadir los argumentos que se escribiran en la terminal
parser.add_argument("Archivo", type = str, help= "Nombre del archivo seguido de .jpg")
parser.add_argument("Escala", type = float, help= "Seleccionar escala: 1, 2, 0.5")

# Declaracion de la bandera time.
group = parser.add_mutually_exclusive_group()
group.add_argument("--time", action = "store_true", help = "print time")

# Parseo de los argumentos
args = parser.parse_args()

# Tiempo inicio del método.
tiempo_inicio = time.perf_counter()

def img(name, esc):
    # escalas disponibles
    val = [1,2,0.5]
    # verifica si el formato es el adecuado y si la escala es soportable
    if (".jpg" in name) and (esc in val):
    # lee la imagen
        img = cv2.imread(name)
    # se obtiene las dimensiones de la imagen original
        #ancho = img.shape[1]
        ancho = int(img.shape[1]*esc)
        alto = int(img.shape[0]*esc)
        dimension = (ancho, alto)
        imgOut = cv2.resize(img, dimension, interpolation=cv2.INTER_CUBIC)
    # despliega la imagen original y la modificada
        cv2.imshow("imagen original", img)
        cv2.imshow("imagen escalada", imgOut)
    # se dejan las imagenes en pantalla hasta presionar alguna tecla
        cv2.waitKey(0)
    # se borran las venatnas creadas
        cv2.destroyAllWindows() 

# Tiempo final del método.        
tiempo_final = time.perf_counter() - tiempo_inicio

# Ejecución del método en la terminal
if __name__ == "__main__":
    img(args.Archivo, args.Escala)
    if args.time:
        print("Tiempo ejecución del método=", tiempo_final)
