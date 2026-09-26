# Punto de entrada del sistema de gestión de la estación espacial.
# Equivalente al bloque "if __name__ == '__main__':" del archivo de EEUU,
# ahora importando Menu a través de la capa de servicio.
from servicios.gestion_misiones import Menu

if __name__ == "__main__":
    menu = Menu()
    menu.ejecutar()
