from R3_1 import llegir_frase, separar_paraules, mezclar_palabras, arxiu_entrada, arxiu_sortida
from R3_2 import crear_directory
from error.log import error_log, tipos_error


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
    tipos_error()


main_error()