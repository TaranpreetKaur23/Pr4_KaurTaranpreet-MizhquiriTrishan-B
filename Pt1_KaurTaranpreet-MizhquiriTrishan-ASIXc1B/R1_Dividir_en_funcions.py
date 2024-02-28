"""
Partint del problema general cal dividir-lo en problemes més simples, denominats subproblemes. Així trobarem les funcions en les quals cal descompondre.
Un punt important, a tenir en compte en aplicar aquesta descomposició, és que cadascun dels subproblemes no es genera
arbitràriament, sinó que es planteja com un objectiu parcial, amb entitat pròpia, per resoldre el seu problema de nivell superior.
Un cop assolits tots aquests objectius parcials, es considera resolt el total.

"""
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

def aleatorio_letras(letras):
    result= ''. join(letras[0] + random.sample(letras[1:], len(letras)-1))
    print(result)
def mostrar_frase_desordenada():
    print()
#end region
obtenir_frase(frase_ordenada)
llegir_frase(frase_ordenada)
paraula = frase_ordenada
separar_paraules(paraula)
letras=paraula
aleatorio_letras(letras)
mostrar_frase_desordenada()