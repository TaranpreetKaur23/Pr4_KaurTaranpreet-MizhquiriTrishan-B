"""
import webbrowser
webbrowser.open("https://example-files.online-convert.com/document/txt/example.txt")
True
"""
"""
import webbrowser

def abrir_url(url):
    try:
        webbrowser.open(url)
        print("URL abierta con éxito.")
    except Exception as e:
        print(f"Error al abrir la URL: {e}")

# Uso de la función
url = "https://chat.openai.com/"
abrir_url(url)
question = input("Introduce tu pregunta: ")  # Esta línea ahora está fuera de la función.

"""
import openai
import os
import pandas as pd
import time

openai.api_key= "sk-8"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

prompt = "<SU CONSULTA>"
response = get_completion(prompt)
print(response)