from enum import Enum


# Enumeración de los posibles estados de una misión.
# Proviene del archivo de EEUU (POO-013.py); el archivo de Rusia (POO-013a.py)
# manejaba el estado como texto plano ("Planificada", "En ejecución", etc.),
# pero se eligió el Enum porque evita errores de escritura y es el tipo de
# dato que usan las subclases de misión conservadas en este proyecto.
class EstadoMision(Enum):
    PLANIFICADA = "Planificada"
    PREPARACION = "En preparación"
    EJECUCION = "En ejecución"
    FINALIZADA = "Finalizada"
