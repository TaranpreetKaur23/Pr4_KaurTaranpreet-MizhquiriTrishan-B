"""
Trishan Mizhquiri
Taranpreet Kaur
08/05/2024
02/05/2024
ASIXc1B UF3 A1 Pt1
main.py
importem els tres fitxers per que es puguin executar les funcions que hi ha en ells.
"""
from R3_1 import *
from R3_2 import *
from error_log import *
import os

def main():
    crear_directory()


main()


def main1():
    ruta = input()
    contenido = leer_archivo(ruta)
    if contenido:
        contenido_desordenado = desordenar_palabras(contenido)
        nombre_archivo = os.path.join("sortida", os.path.basename(ruta).split('.')[0] + "_boges.txt")
        escribir_archivo_sortida(contenido_desordenado, nombre_archivo)
main1()