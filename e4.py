"""
Taranpreet Kaur
Trishan Mizhquiri
29/11/2023
ASIXc 1B UF1 PR4
Programa que imprimeix un tauler d’escacs per pantalla. Un taulell d’escacs comença amb
la casella Blanca i és de mida 8x8 sempre ;-)

"""
blanc = "⬜"
negre = "⬛"
for i in range(1,8):
    for j in range(i+1):
        print(blanc,negre,end="")
    print()