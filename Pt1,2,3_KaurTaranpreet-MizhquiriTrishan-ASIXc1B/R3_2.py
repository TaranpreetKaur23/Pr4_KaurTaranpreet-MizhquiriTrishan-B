"""
Trishan Mizhquiri
Taranpreet Kaur
08/05/2024
02/05/2024
ASIXc1B UF3 A1 Pt1
R3_2
crea el fitxer ./sortida per el arxiu de sortida y el fitxer ./log per el fitxer de errores.
"""
import os
def crear_directory():
    directorios = ["sortida", "log"]
    for directorio in directorios:
        if not os.path.exists(directorio):
            os.makedirs(directorio)


crear_directory()
