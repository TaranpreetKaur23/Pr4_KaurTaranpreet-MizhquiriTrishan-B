"""
Trishan Mizhquiri
Taranpreet Kaur
02/05/2024
ASIXc1B UF3 A1 Pt1
R3_1
abre el arxiu entrada cualquier arxiu txt y envia su contenido a un nuevo archivo  de
sallida llamado sortida donde debemos colocar los arxius _boges.txt  con las palabras desordenadas.
"""
import os
import random
from datetime import datetime
from error_log import registrar_error
def leer_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        registrar_error("No se encontró el archivo.")
    except Exception as e:
        registrar_error(f"Error: {e}")

def escribir_archivo_sortida(contenido_desordenado, nombre_archivo):
    try:
        with open(nombre_archivo, "wt") as fs:
            for palabra in contenido_desordenado:
                fs.write(palabra + "\n")
    except Exception as e:
        registrar_error(f"No se pudo escribir en el archivo de salida: {e}")

def desordenar_palabras(contenido):
    palabras = contenido.split()
    palabras_desordenadas = []
    for palabra in palabras:
        if len(palabra) <= 2:
            palabras_desordenadas.append(palabra)
        else:
            primera_letra = palabra[0]
            ultima_letra = palabra[-1]
            letras_intermedias = list(palabra[1:-1])
            random.shuffle(letras_intermedias)
            palabra_desordenada = primera_letra + ''.join(letras_intermedias) + ultima_letra
            palabras_desordenadas.append(palabra_desordenada)
    return palabras_desordenadas

def registrar_error(error):
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("log/boges.log", "a") as f:
        f.write(f"{timestamp} - {error}\n")
