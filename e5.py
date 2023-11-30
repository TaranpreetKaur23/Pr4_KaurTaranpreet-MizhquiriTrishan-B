"""
Taranpreet Kaur
Trishan Mizhquiri
29/11/2023
ASIXc 1B UF1 PR4
Programa que realitza la multiplicació, de dos
nombres sencers,  mitjançant sumes.
"""
try:
    resultat=0

    numero1= int(input("Escriu el primer numero: "))
    numero2=int(input("Escriu el segon numero: "))

    for i in range(numero2):
        resultat += numero1
    print(f"El resultado de sumar {numero2} veces el numero {numero1} és: {resultat}")
except ValueError:
    print("No funciona")
