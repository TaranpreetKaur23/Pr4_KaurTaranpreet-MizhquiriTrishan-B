"""
Taranpreet Kaur
Trishan Mizhquiri
29/11/2023
ASIXc 1B UF1 PR4
Programa que mostra per pantalla la suma de tots els nombres senars i de tots els
nombres parells inferiors a un número límit, que l’usuari introdueix per teclat.
"""
try:
    suma=int(input("Introdueix límit: "))
    for i in range(suma,2):
        sumaparells=i
        print(sumaparells," ", end="")
except ValueError:
    print("NO FUNCIONA BOBO QUE ERES")
