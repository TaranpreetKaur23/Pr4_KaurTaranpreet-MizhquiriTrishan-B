
import random

frase_ordenada = input(" ")

def obtenir_frase(frase_ordenada):
    print(frase_ordenada)
def llegir_frase(frase_ordenada):
    paraula = frase_ordenada.split()
    print(paraula)

def separar_paraules(paraula):
    letras = [letter for word in paraula for letter in word]
    print(letras)

def scramble_word(word):
    # Get the first and last letters of the word.
    first_letter = word[0]
    last_letter = word[-1]
    # Get the middle letters of the word.
    middle_letters = word[1:-1]
    # Shuffle the middle letters.
    random.shuffle(middle_letters)
    # Return the scrambled word.
    scrambled_word = first_letter
    for letter in middle_letters:
        scrambled_word += letter
    scrambled_word += last_letter
    return scrambled_word
def mostrar_frase_desordenada():
    print()
#end region
obtenir_frase(frase_ordenada)
llegir_frase(frase_ordenada)
paraula = frase_ordenada
separar_paraules(paraula)
word=paraula
scramble_word(word)
mostrar_frase_desordenada()
