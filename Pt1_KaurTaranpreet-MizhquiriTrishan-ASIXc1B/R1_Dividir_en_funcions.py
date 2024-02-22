"""
Partint del problema general cal dividir-lo en problemes més simples, denominats subproblemes. Així trobarem les funcions en les quals cal descompondre.
Un punt important, a tenir en compte en aplicar aquesta descomposició, és que cadascun dels subproblemes no es genera
arbitràriament, sinó que es planteja com un objectiu parcial, amb entitat pròpia, per resoldre el seu problema de nivell superior.
Un cop assolits tots aquests objectius parcials, es considera resolt el total.

"""

frase_ordenada = input(" ")

def obtenir_frase(frase_ordenada):
    print(frase_ordenada)
def llegir_frase(frase_ordenada):
    paraula = frase_ordenada.split()
    print(paraula)

def separar_paraules(paraula):
    letras = [letter for word in paraula for letter in word]
    print(letras)
    return letras

"""    
def fijar_pri_ult():
def aleatorio_letras():

def mostrar_frase_desordenada():
"""
#end region
obtenir_frase(frase_ordenada)
llegir_frase(frase_ordenada)
paraula = frase_ordenada
separar_paraules(paraula)
"""
fijar_pri_ult()
aleatorio_letras()
mostrar_frase_desordenada()
"""