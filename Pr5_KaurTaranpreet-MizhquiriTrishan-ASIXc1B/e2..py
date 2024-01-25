"""
Taranpreet Kaur
Trishan Mizhquiri
24/01/2024
ASIXc 1B UF1 PR5
Programa que generi una llista de 100 nombres aleatoris entre 1 i 50. Obtenir la mitja dels
nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars.
"""
try:

    import random

    numeros = [random.randint(0, 50) for _ in range (100)]
    print(numeros, end=", ")
    print()

    numeros_pares = sum(numeros[::2]) / len(numeros[::2])
    print(f"La media de los numeros pares es: {numeros_pares:.2f}")

    numeros_impares = sum(numeros[1::2]) / len(numeros[1::2])
    print(f"La media de los numeros impares es: {numeros_impares:.2f}")

except ValueError:
    print("No Funciona")