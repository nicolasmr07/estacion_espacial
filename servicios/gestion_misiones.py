# En ninguno de los dos archivos originales existía una separación entre
# "menú" (interfaz de consola) y "servicio de gestión de misiones" (lógica de
# negocio): en el archivo de EEUU ambas cosas estaban juntas en la clase
# Menu, y en el archivo de Rusia, juntas en la función menu(). Como la
# estructura obligatoria exige un archivo utils/menu.py y, además, un archivo
# servicios/gestion_misiones.py, y las restricciones no permiten crear
# clases, métodos ni funciones nuevas, este módulo actúa como el punto de
# acceso de la capa de "servicio": expone la clase Menu (definida en
# utils/menu.py) para que main.py gestione las misiones a través de él,
# sin duplicar ni modificar su lógica.
from utils.menu import Menu
