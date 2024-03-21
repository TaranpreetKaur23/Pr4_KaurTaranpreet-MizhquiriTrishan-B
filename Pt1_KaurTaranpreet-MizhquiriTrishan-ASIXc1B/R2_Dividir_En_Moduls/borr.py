def getdatafromkeyboard():
    """ Aquesta funció recull les dades des del teclat.
    Retorna: una única cadena de caràcters.
    """
    print("Introdueix les dades (i prem Enter per a finalitzar):")
    dades = input()
    return dades

def getdatafrom_server(URL):
    URL = "https://example-files.online-convert.com/document/txt/example.txt"
    import requests
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error en obtenir dades des del servidor: {e}")
        return None

def getdatafrom_chatGPT(question):
    question = "https://chat.openai.com/"
    return question

def getdatafromfile(filename):
    """ Aquesta funció recull les dades des d'un arxiu.
    Entrada: Una cadena de caràcters amb el nom del fitxer origen.
    Retorna: una única cadena de caràcters.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            dades = file.read()
        return dades
    except FileNotFoundError:
        print("L'arxiu no s'ha trobat.")
        return None
    except IOError as e:
        print(f"Error en llegir l'arxiu: {e}")
        return None