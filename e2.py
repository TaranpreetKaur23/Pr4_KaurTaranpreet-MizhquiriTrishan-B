"""
Taranpreet Kaur
Trishan Mizhquiri
29/11/2023
ASIXc 1B UF1 PR4
Programa que mostra un triangle amb nombres a les cantonades.
Cal demanar quina alçada ha de tenir el triangle.
Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
"""
try:
    triangle=int(input("Escriu l'alçada de piràmide que vols: "))
    for x in range(1, triangle+1):
        for j in range(x):
            print(x,end=" ")
        print(  )
except ValueError:
    print("NO FUNCIONA TONTO")