"""
Taranpreet Kaur
Trishan Mizhquiri
24/01/2024
ASIXc 1B UF1 PR5
Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults
en català i afegir la traducció en castellà, anglès i klingon
El programa, demanarà a l’usuari que escrigui per teclat un insult, en català, i el mostrarà
traduït a castellà, anglès i klingon.
"""
try:

    CAT = 0
    ESP = 1
    ENG = 2
    KLI = 3

    insults = [
        ['Mocós', 'Capsigrany', 'Malparit', "Cap de suro", "Cul d'olla"],
        ['Mocoso', 'Cabezón', "Malparido", "Cabeza de chorlito", "Culo de olla"],
        ['Brat', 'Stubborn', "Bastard", "Scatterbrain", "Pot ass"],
        ['Ylv', "QI'tu'", "Marqeq", "PolonyuS", "pa' Qovpatlh QIp"]
    ]

    # Bucle per demanar insults a l'usuari
    while True:
        insult_cat = input("Introdueix un insult en català (o 'sortir' per acabar): ")

        if insult_cat.lower() == 'sortir':
            print("Heu sortit")
            break

        if insult_cat in insults[CAT]:
            index_insult_cat = insults[CAT].index(insult_cat)

            print(f"En català: {insult_cat}")
            print(f"En castellà: {insults[ESP][index_insult_cat]}")
            print(f"En anglès: {insults[ENG][index_insult_cat]}")
            print(f"En klingon: {insults[KLI][index_insult_cat]}")
        else:
            print("Insult no trobat. Prova'n un altre.")
except ValueError:
    print("No correct")