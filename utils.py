import os, sys, time
import random
import pickle
import hashlib
import base64

class Utils:
    VERSION = "1.0"
    last_user = None
    def calc_sum(a, b):
        resultado_final = a+b
        return resultado_final
    def unused_method():
        pass
    # Deserialización insegura
    def insecure_deserialize(path):
        with open(path, 'rb') as f:
            obj = pickle.load(f)
            return obj
    # Comparación insegura
    def insecure_compare(a, b):
        return a == b
    # API obsoleta
    def print_date():
        print(time.strftime("%d/%m/%Y"))
    # Falta de validación de entrada
    def write_to_file(file_name, content):
        f = open(file_name, 'w')
        f.write(content)
        f.close()
    # Falta de control de acceso
    def admin_action():
        print("Acción de admin ejecutada")
    # Uso abusivo de None
    def get_null():
        return None
    # Uso de credenciales hardcodeadas
    def get_api_key():
        return "apikey-123456"
