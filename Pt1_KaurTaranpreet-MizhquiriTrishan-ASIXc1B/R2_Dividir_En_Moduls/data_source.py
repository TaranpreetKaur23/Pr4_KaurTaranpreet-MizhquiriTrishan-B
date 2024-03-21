def get_data__from_keyboard():
    print ("Introdueix les dades (i prem Enter per a finalitzar):")
    dades = input()
    return dades

import requests
def get_data_from_server(URL):
    URL = "https://example-files.online-convert.com/document/txt/example.txt"
    dades = get_data_from_server(URL)
    print(dades)
    response = requests.get(URL)
    response.raise_for_status()
    return response.text
def get_data_from_chatGPT(questio):
    questio = "https://chat.openai.com/"
    return questio