from abc import ABC, abstractmethod

from modelos.estado_mision import EstadoMision


# Clase base de las misiones. Guarda los datos que comparten y deja que cada
# tipo de misión implemente cómo se inicia y cómo se finaliza.
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

    # El código solo puede tener números.
    def set_codigo(self, codigo):
        if codigo.isdigit():
            self.__codigo = codigo
        else:
            print("El código debe contener únicamente números.")

    # El nombre debe tener letras y espacios.
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
