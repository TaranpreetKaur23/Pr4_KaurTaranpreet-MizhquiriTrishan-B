"""
Taranpreet Kaur
Trishan Mizhquiri
29/11/2023
ASIXc 1B UF1 PR4
Programa que mostra per pantalla la suma de tots els nombres senars i de tots els
nombres parells inferiors a un número límit, que l’usuari introdueix per teclat.
"""
try:
    suma_parells = 0
    suma_senars = 0

    limit = int(input("Introdueix un número límit: "))

    for i in range(limit):
        if i % 2 == 0:
            suma_parells += i
        else:
            suma_senars += i

    print(f"Si el límit és {limit}, sumaParells {suma_parells} i sumaSenars {suma_senars}")
except ValueError:
    print("NO FUNCIONA BOBO QUE ERES")
