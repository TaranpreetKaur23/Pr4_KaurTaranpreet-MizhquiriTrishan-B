"""
Trishan Mizhquiri
Taranpreet Kaur
ASIXc1B UF3 A1 Pt1
R3.1
abre el arxiu paraules.txt y envia su contenido a un nuevo archivo  de sallida llamado paraules_boges.txt
en otro arxivo llamado boges.log deben poner los errores: debug, info, warning, error, crtical
"""
import datetime as dt
import logging
ruta = input()
def arxiu_entrada():
    with open(ruta, "rt") as fitxer_entrada:
        paraules = fitxer_entrada.read()
    return paraules

def arxiu_sortida():
    with open("paraules_boges.txt", "wt") as fitxer_sortida:
        fitxer_sortida.write(arxiu_entrada())

def error_log():
    data = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    data_ini = dt.datetime
    


arxiu_entrada()
arxiu_sortida()