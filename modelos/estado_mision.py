from enum import Enum


# Estados posibles de una misión.
class EstadoMision(Enum):
    PLANIFICADA = "Planificada"
    PREPARACION = "En preparación"
    EJECUCION = "En ejecución"
    FINALIZADA = "Finalizada"
