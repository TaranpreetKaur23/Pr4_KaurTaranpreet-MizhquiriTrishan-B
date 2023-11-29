"""
Taranpreet Kaur
Trishan Mizhquiri
29/11/2023
ASIXc 1B UF1 PR4
#Programa que demana a l'usuari la introducció de 10 nombres sencers (que també
#podrien ser 10000000 😱😳😈) i ha de mostrar, al final i per pantalla, quants són positius,
#quants negatius i quants zero.
"""
positivo=0
negativo=0
Zero=0

try:
    for x in range(10):
        numero = int(input("Escriu 10 nombres sencers: "))
        if numero < 0:
            negativo+=1
        elif numero > 0:
            positivo+=1
        else: # numero == 0:
            Zero+=1
    print(positivo, "numeros son positivos")
    print(negativo, "numeros son negativos")
    print(Zero, "numeros son zeros")
except ValueError:
    print("No funciona CARA ALCACHOFA")