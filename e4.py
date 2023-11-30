"""
Taranpreet Kaur
Trishan Mizhquiri
29/11/2023
ASIXc 1B UF1 PR4
Programa que imprimeix un tauler d’escacs per pantalla. Un taulell d’escacs comença amb
la casella Blanca i és de mida 8x8 sempre ;-)

"""
try:
    BLANC = "⬜"
    NEGRE = "⬛"

    for i in range(8):
        for j in range(8):
            casella = BLANC
            if (i + j) % 2 != 0:
                casella = NEGRE
            print(casella, end="")
        print()
except ValueError:
    print("No funciona")
