"""
Trishan Mizhquiri
Taranpreet Kaur
08/05/2024
02/05/2024
ASIXc1B UF3 A1 Pt1
main.py
importem els tres fitxers per que es puguin executar les funcions que hi ha en ells.
"""
from R3_1 import llegir_frase, separar_paraules, mezclar_palabras, arxiu_entrada, arxiu_sortida
from R3_2 import crear_directory
from error_log import error_log


def main():
    crear_directory()
    main()


def main1():
    frase_ordenada = arxiu_entrada()
    paraula = llegir_frase(frase_ordenada)
    separar_paraules(paraula)
    palabras_desordenadas = mezclar_palabras(paraula)
    arxiu_sortida(palabras_desordenadas)


if __name__ == "__main__":
    main1()


def main_error():
    error_log()


main_error()