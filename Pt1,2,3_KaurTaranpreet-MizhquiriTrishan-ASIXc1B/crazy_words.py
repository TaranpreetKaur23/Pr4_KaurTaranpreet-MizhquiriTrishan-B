from R1_Dividir_en_funcions import llegir_frase, separar_paraules, mezclar_palabras, mostrar_frase_desordenada


def crazy_words():
    frase_ordenada = input()
    paraula = llegir_frase(frase_ordenada)
    separar_paraules(paraula)
    frase_desordenada = mezclar_palabras(paraula)
    mostrar_frase_desordenada(frase_desordenada)


crazy_words()