"""
Partint del problema general cal dividir-lo en problemes més simples, denominats subproblemes. Així trobarem les funcions en les quals cal descompondre.
Un punt important, a tenir en compte en aplicar aquesta descomposició, és que cadascun dels subproblemes no es genera
arbitràriament, sinó que es planteja com un objectiu parcial, amb entitat pròpia, per resoldre el seu problema de nivell superior.
Un cop assolits tots aquests objectius parcials, es considera resolt el total.

"""
import random
frase_ordenada = input("Introduce una frase: ")
def obtenir_frase(frase_ordenada):
    print(frase_ordenada)

def llegir_frase(frase_ordenada):
    paraules = frase_ordenada.split()
    return paraules

def separar_paraules(paraules):
    letras = [letter for word in paraules for letter in word]
    return letras

def mezclar_palabras(paraules):
    palabras_mezcladas = []
    for palabra in paraules:
        if len(palabra) > 0:
            inicio = palabra[0]
            medio = list(palabra[1:-1])
            random.shuffle(medio)
            fin = palabra[-1]
            palabra_mezclada = inicio + ''.join(medio) + fin
            palabras_mezcladas.append(palabra_mezclada)
        else:
            palabras_mezcladas.append(palabra)
    return palabras_mezcladas

def mostrar_frase_desordenada(palabras_mezcladas):
    frase_desordenada = ' '.join(palabras_mezcladas)
    print("\nFrase con letras intermedias desordenadas:")
    print(frase_desordenada)

# end region
obtenir_frase(frase_ordenada)
paraula = llegir_frase(frase_ordenada)
letras = separar_paraules(paraula)
frase_desordenada = mezclar_palabras(paraula)
mostrar_frase_desordenada(frase_desordenada)
