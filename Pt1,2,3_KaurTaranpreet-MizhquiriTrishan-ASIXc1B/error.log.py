import logging


def guardar_log(log_linia):
    ruta_log = "log/boges.txt"
    with open(ruta_log, "at") as log:
        log.write(log_linia + "\n")
def Error_log():
    with open("paraules_boges.txt", "at") as log:
        f_error.write(message+"\n")
        logging.basicConfig(level=logging)
def tipo_error():
    error_log =("logging.INFO")
    "info message"
    logging.DEBUG
    logging.WARNING
    logging.ERROR
    logging.CRITICAL
def procesar_log(linea):
    patron_log_apache = re.compile(r'(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (\d+)')
    patron_log_simple = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (\S+) - (\S+) - (.*)')

    if patron_log_apache.match(linea):
        print("Log de Apache detectado:")
        # Aquí puedes incluir el código para procesar el log de Apache
    elif patron_log_simple.match(linea):
        print("Log simple detectado:")
        # Aquí puedes incluir el código para procesar el log simple
    else:
        print("Error: formato de log no reconocido")

def ejemplo_apache():
    log_linea = '127.0.0.1 user-identifier frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 208'
    procesar_log(log_linea)

def ejemplo_simple():
    log_linea = '2022-04-19 15:10:26,618 - simple_example - DEBUG - debug message'
    procesar_log(log_linea)

    log_linea = '2022-04-19 15:10:26,620 - simple_example - INFO - info message'
    procesar_log(log_linea)

    log_linea = '2022-04-19 15:10:26,695 - simple_example - WARNING - warn message'
    procesar_log(log_linea)

    log_linea = '2022-04-19 15:10:26,697 - simple_example - ERROR - error message'
    procesar_log(log_linea)

    log_linea = '2022-04-19 15:10:26,773 - simple_example - CRITICAL - critical message'
    procesar_log(log_linea)
