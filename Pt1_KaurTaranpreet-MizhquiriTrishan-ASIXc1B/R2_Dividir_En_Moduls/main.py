"""
import webbrowser
webbrowser.open("https://example-files.online-convert.com/document/txt/example.txt")
True
"""

import openai

def abrir_url(url):
    try:
        openai.completion.create(url)
        print("URL abierta con éxito.")
    except Exception as e:
        print(f"Error al abrir la URL: {e}")

# Uso de la función
url = "https://chat.openai.com/"
abrir_url(url)
question = input("Introduce tu pregunta: ")  # Esta línea ahora está fuera de la función.
