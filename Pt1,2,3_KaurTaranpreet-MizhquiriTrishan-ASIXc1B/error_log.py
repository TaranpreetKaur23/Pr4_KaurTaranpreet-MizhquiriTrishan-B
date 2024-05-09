import logging
from datetime import datetime

def iniciar_registro():
    logging.basicConfig(filename='log/boges.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def registrar_info(mensaje):
    logging.info(mensaje)

def registrar_debug(mensaje):
    logging.debug(mensaje)

def registrar_warning(mensaje):
    logging.warning(mensaje)

def registrar_error(mensaje):
    logging.error(mensaje)

def registrar_critical(mensaje):
    logging.critical(mensaje)