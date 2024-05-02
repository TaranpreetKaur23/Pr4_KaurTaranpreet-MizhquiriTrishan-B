"""
En aquest lliurament cal aprofitar tota la feina feta fins ara, és a dir el R1_Dividir_en_funciones
i crazy_word, main, data_source lliurament i afegir el tractament de fitxers.
Per tant, les dades caldrà agafar-les d’un arxiu d’entrada. I la sortida, que generi el programa
caldrà escriure-la en un altre arxiu de sortida. L’aplicació NO ha de tenir menú, l’execució es
“desatesa” i els resultats, o estan a arxius de sortida o als de log.
Arxiu d’entrada: 	paraules.txt esta en la carpeta entrada del projecte
Arxiu de sortida: 	paraules_boges.txt
Arxiu d’errors: 	boges.log

boges.log servirà per mostrar tota informació, error… relacionat amb el funcionament del programa.
És a dir, informarà de quan s’ha iniciat el programa i quan ha acabat, a part dels errors /
problemes trobats o qualsevol altra dada que es considera important.

Aquest arxiu log, no es podrà sobreescriure, haurà d’acumular un “històric” de tota la informació
de les diferents execucions del programa
"""
import datetime as dt
import os
f=open("boges.log", "at")
def arxiu_sortida():
    with open("paraules_boges.txt", "at") as fitxer_sortida:
        fitxer_sortida.write(f"{arxiu_entrada()} \n")

def error_log():
    data = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    data_ini = dt.datetime.now()
    temps_transcorregut = dt.datetime.now() - data_ini
    if not os.path.isdir(arxiu_entrada()):
        f.write(f"{data} - Error: el directori especific no existe. - {temps_transcorregut} \n")
        f.close()
        return
    if not os.access(arxiu_entrada(), os.R_OK):
        f.write(f"{fecha} - Error: El directorio no tiene permisos de lectura para tu usuario. - {tiempo_transcurrido} \n")
        f.close()
        return
    if not os.access(arxiu_sortida(), os.W_OK):
        f.write(f"{data} - Error: El directorio no tiene permisos de escritura para tu usuario. - {temps_transcorregut} \n")
        f.close()
        return
    if not os.access(arxiu_sortida(), os.X_OK):
        f.write(f"{data} - Error: El directorio no tiene permisos de ejecucion para tu usuario. - {temps_transcorregut} \n")
        f.close()
        return
    else:
        f.write(f"{data} - Inici del programa - {temps_transcorregut} \n")
        f.write(f"{data} - Fi del programa - {temps_transcorregut} \n")
        f.close()
        return