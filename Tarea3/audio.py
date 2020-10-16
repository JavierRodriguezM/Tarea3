#!/usr/bin/python
from playsound import playsound
import argparse
import time
# Función: Recibe un audio y lo reproduce n veces
# Entradas: Nombre del audio y el número de veces que se desea reproducir
# Salida: El audio n veces reproducido


# Instrucción para inicializar el parser
parser = argparse.ArgumentParser(description = "Reproduce un audio en formato mp3")


# Añadir los argumentos que se escribiran en la terminal
parser.add_argument("Audio", type = str, help= "Nombre del archivo de audio")
parser.add_argument("Reproducciones", type = int, help= "Cantidad de veces que se quiera reproducir el audio")

# Declaracion de la bandera time.
group = parser.add_mutually_exclusive_group()
group.add_argument("--time", action = "store_true", help = "Tiempo de ejecución del método")


# Parseo de los argumentos
args = parser.parse_args()

# Tiempo inicio del método.
tiempo_inicio = time.perf_counter()

def sound(audio, n):
    if (".mp3" in audio):
        for i in range(0,n):
            playsound(audio)

# Tiempo final del método.        
tiempo_final = time.perf_counter() - tiempo_inicio

# Ejecución del método en la terminal
if __name__ == "__main__":
    sound(args.Audio, args.Reproducciones)
    if args.time:
        print("Tiempo ejecución del método=", tiempo_final)
