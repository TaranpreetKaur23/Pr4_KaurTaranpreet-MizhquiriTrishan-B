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
    if 2<=triangle<=9:
        for x in range(triangle):
            for j in range(x+1):
                if x == triangle -1 or (j==0 or j==x):
                    print(f"{x+1}", end=" ")
                else:
                    print("", end="  ")
            print()
            if x != triangle:
               print()
    else:
        print("L'alçada ha de ser de 2 a 9")
except ValueError:
    print("NO FUNCIONA TONTO")