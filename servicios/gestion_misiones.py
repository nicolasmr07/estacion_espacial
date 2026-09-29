# En ninguno de los dos archivos originales existía una separación entre
# "menú" (interfaz de consola) y "servicio de gestión de misiones" (lógica de
# negocio): en el archivo de EEUU ambas cosas estaban juntas en la clase
# Menu, y en el archivo de Rusia, juntas en la función menu(). 
# 
# Este módulo actúa como el punto de
# acceso de la capa de "servicio": expone la clase Menu (definida en
# utils/menu.py) para que main.py gestione las misiones a través de él
from utils.menu import Menu