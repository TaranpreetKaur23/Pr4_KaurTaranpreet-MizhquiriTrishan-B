def getDataFromKeyboard():
    print("Introdueix les dades (i prem Enter per a finalitzar):")
    dades = input()
    return dades


import requests


def getDataFromServer():
    URL = "https://example-files.online-convert.com/document/txt/example.txt"
    dades = getDataFromServer()
    print(dades)
    response = requests.get(URL)
    response.raise_for_status()
    return response.text


def getDataFromChatGPT():
    questio = "https://chat.openai.com/"
    return questio


def get_data__from_server():
    return None
