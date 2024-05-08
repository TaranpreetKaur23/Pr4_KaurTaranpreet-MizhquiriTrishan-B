"""
Trishan Mizhquiri
Taranpreet Kaur
ASIXc1B UF3 A1 Pt1
R3.1
abre el arxiu paraules.txt y envia su contenido a un nuevo archivo  de
sallida llamado paraules_boges.txt con las palabras desordenadas.
"""
import random

def llegir_frase(frase_ordenada):
    # Function to read the phrase from the input file
    return frase_ordenada.split()

def separar_paraules(paraula):
    # Function to separate words from the phrase
    return paraula

def mezclar_palabras(paraula):
    # Function to shuffle letters of each word except the first and last letter
    palabras_desordenadas = []
    for palabra in paraula:
        if len(palabra) <= 2:
            palabras_desordenadas.append(palabra)  # Words with 2 or fewer letters remain unchanged
        else:
            middle_part = list(palabra[1:-1])  # Get the middle part of the word
            random.shuffle(middle_part)  # Shuffle the middle part
            palabra_desordenada = palabra[0] + ''.join(middle_part) + palabra[-1]  # Concatenate first letter, shuffled middle part, and last letter
            palabras_desordenadas.append(palabra_desordenada)
    return palabras_desordenadas

def arxiu_entrada():
    # Read content from input file
    ruta = "entrada/paraules.txt"
    with open(ruta, "rt") as fitxer_entrada:
        paraules = fitxer_entrada.read()
    return paraules

def arxiu_sortida(frase_desordenada):
    # Write scrambled words to the output file
    with open("paraules_boges.txt", "wt") as fs:
        for word in frase_desordenada:
            fs.write(word + "\n")  # Write each word in a new line

def main():
    # Main function to orchestrate the process
    frase_ordenada = arxiu_entrada()
    paraula = llegir_frase(frase_ordenada)
    separar_paraules(paraula)
    palabras_desordenadas = mezclar_palabras(paraula)
    print(palabras_desordenadas)
    arxiu_sortida(palabras_desordenadas)