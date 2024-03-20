"""
Taranpreet Kaur
Trishan Mizhquiri
24/01/2024
ASIXc 1B UF1 PR5
Programa que generi una llista de 100 nombres aleatoris entre 1 i 50. Obtenir la mitja dels
nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars.
"""
import random
limitInferior = 0
limitSuperior = 50

numeros = int(random.randint(limitInferior, limitSuperior))
    for x in range(100):
     print(numeros, end=", ")
     numeros_pares = [num for num in x if num % 2 == 0]
     print(f"{numeros_pares:.2f}")
