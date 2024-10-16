
from random import randint, choices
import time
import datetime

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__timestamp = time.localtime()  # Marca de tiempo exacta para el paciente

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_timestamp(self):
        return self.__timestamp
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        # convertimos el timestamp a formato legible (hora: minuto)
        hora_ingreso = time.strftime('%H:%M:%S',self.__timestamp) # al chorro de cosas, lo transformamos solo en horas minutos y segundos (hasta segundos porque el sleep del main es 1 s)
        # devolvemos el nombre, riesgo, descripción y hora de ingreso a partir del timestamp
        cad = f"{self.__nombre} {self.__apellido}\t -> {self.__riesgo}-{self.__descripcion} {hora_ingreso}"
        return cad
