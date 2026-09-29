from abc import ABC, abstractmethod

from modelos.estado_mision import EstadoMision


# Superclase abstracta de toda misión.
#
# Base tomada del archivo de EEUU: usa el Enum EstadoMision y solo maneja
# los atributos "codigo" y "nombre", que son los que comparten todas las
# subclases conservadas (MisionExploracion, MisionInvestigacion, MisionRescate).
#
# Del archivo de Rusia se conservan, tal cual, los métodos set_codigo() y
# set_nombre(), porque son funcionalidad exclusiva de ese archivo (validación
# de que el código sea numérico y el nombre solo contenga letras/espacios) y
# operan únicamente sobre atributos que ya existen aquí (codigo, nombre), por
# lo que no requieren crear atributos nuevos.
#
# NO se conservan set_destino(), set_duracion(), get_destino() ni
# get_duracion() del archivo de Rusia: esos métodos dependen de los atributos
# "destino" y "duracion", que pertenecían a la clase MisionEspacial de Rusia.
# Esa clase no existe en la idea del codigo actual (que exige mision_exploracion.py, 
# mision_investigacion.py y mision_rescate.py, propios de EEUU), y agregar esos 
# atributos a la jerarquía elegida crearia atributos nuevos.
class Mision(ABC):
    def __init__(self, codigo, nombre):
        self.__codigo = codigo.strip()
        self.__nombre = nombre.strip()
        self.__estado = EstadoMision.PLANIFICADA

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado: EstadoMision):
        self.__estado = estado

    # Exclusivo del archivo de Rusia: valida que el código sea únicamente numérico.
    def set_codigo(self, codigo):
        if codigo.isdigit():
            self.__codigo = codigo
        else:
            print("El código debe contener únicamente números.")

    # Exclusivo del archivo de Rusia: valida que el nombre contenga solo letras y espacios.
    def set_nombre(self, nombre):
        palabras = nombre.split()
        valido = True
        for palabra in palabras:
            if not palabra.isalpha():
                valido = False
                break
        if valido and len(palabras) > 0:
            self.__nombre = nombre
        else:
            print("El nombre debe contener únicamente letras y espacios.")

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def finalizar(self):
        pass
