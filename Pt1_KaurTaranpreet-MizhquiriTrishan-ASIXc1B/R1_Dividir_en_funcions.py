"""
Partint del problema general cal dividir-lo en problemes més simples, denominats subproblemes. Així trobarem les funcions en les quals cal descompondre.
Un punt important, a tenir en compte en aplicar aquesta descomposició, és que cadascun dels subproblemes no es genera
arbitràriament, sinó que es planteja com un objectiu parcial, amb entitat pròpia, per resoldre el seu problema de nivell superior.
Un cop assolits tots aquests objectius parcials, es considera resolt el total.

"""
import random

def obtenir_frase(frase):
    print(frase)

def llegir_frase(frase):
    paraules = frase.split()
    return paraules

def separar_paraules(paraules):
    letras = [letter for word in paraules for letter in word]
    return letras

def aleatorio_letras(letras):
    shuffled_letras = [letras[0]] + random.sample(letras[1:], len(letras)-1)
    result = ''.join(shuffled_letras)
    return result

def mostrar_frase_desordenada(frase_desordenada):
    print(frase_desordenada)

# Main execution flow
frase_ordenada = input("Introduce una frase: ")
obtenir_frase(frase_ordenada)
paraula = llegir_frase(frase_ordenada)
letras = separar_paraules(paraula)
frase_desordenada = aleatorio_letras(letras)
mostrar_frase_desordenada(frase_desordenada)
