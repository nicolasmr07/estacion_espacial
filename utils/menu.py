import time

from modelos.estacion_espacial import EstacionEspacial
from modelos.mision_exploracion import MisionExploracion
from modelos.mision_investigacion import MisionInvestigacion
from modelos.mision_rescate import MisionRescate


# Clase que representa el menú interactivo por consola.
#
# Es la funcionalidad que estaba duplicada conceptualmente en ambos archivos
# (Menu.ejecutar() en EEUU y menu() en Rusia). Se conserva la lógica de
# registro de misiones de EEUU tal cual (opción "1"), porque es la única
# compatible con las subclases de Mision elegidas (pide planeta/area/
# tripulación según el tipo). A esa base se le agregan, sin modificar su
# lógica interna, las opciones exclusivas de Rusia: buscar misión, cambiar
# estado y mostrar resumen (opciones "3", "4" y "5"), renumerando el menú
# para que todas las funcionalidades de ambos archivos convivan.
class Menu:
    def __init__(self):
        self.estacion = EstacionEspacial()

    def ejecutar(self):
        while True:
            print("\n🌌 --- MENÚ PRINCIPAL ---")
            print("1. Agregar misión")
            print("2. Mostrar misiones")
            print("3. Buscar misión")
            print("4. Cambiar estado")
            print("5. Mostrar resumen")
            print("6. Iniciar misión")
            print("7. Finalizar misión")
            print("0. Salir")

            opcion = input("Seleccione opción: ")
            if not opcion.isdigit():
                print("Debe ingresar un número.")
                continue

            match int(opcion):
                # --- Registrar misión (lógica original de EEUU, sin cambios) ---
                case 1:
                    nombre = input("Nombre de la misión: ")
                    if not nombre.replace(" ", "").isalpha():
                        print("El nombre debe contener solo letras.")
                        continue
                    codigo = input("Código de la misión: ")
                    if not codigo.isdigit():
                        print("El código debe ser numérico.")
                        continue
                    tipo = input("Tipo de misión (exploracion/investigacion/rescate): ").lower()
                    if tipo == "exploracion":
                        planeta = input("Planeta de exploración: ")
                        mision = MisionExploracion(codigo, nombre, planeta)
                    elif tipo == "investigacion":
                        area = input("Área científica: ")
                        mision = MisionInvestigacion(codigo, nombre, area)
                    elif tipo == "rescate":
                        tripulacion = input("Tripulación a rescatar: ")
                        mision = MisionRescate(codigo, nombre, tripulacion)
                    else:
                        print("Tipo inválido.")
                        continue
                    self.estacion.agregar_mision(mision)

                # --- Mostrar misiones (lógica original de EEUU, sin cambios) ---
                case 2:
                    self.estacion.mostrar_misiones()

                # --- Buscar misión (funcionalidad exclusiva de Rusia) ---
                case 3:
                    print("\n1. Buscar por código")
                    print("2. Buscar por nombre")
                    opcion_busqueda = input("Seleccione una opción: ")
                    if not opcion_busqueda.isdigit():
                        print("Debe ingresar un número.")
                        continue
                    match int(opcion_busqueda):
                        case 1:
                            codigo = input("Ingrese el código: ")
                            mision = self.estacion.buscar_por_codigo(codigo)
                            if mision is not None:
                                print(f"Código: {mision.get_codigo()}, Nombre: {mision.get_nombre()}, "
                                      f"Estado: {mision.get_estado().value}")
                            else:
                                print("No se encontró la misión.")
                        case 2:
                            nombre = input("Ingrese el nombre: ")
                            mision = self.estacion.buscar_por_nombre(nombre)
                            if mision is not None:
                                print(f"Código: {mision.get_codigo()}, Nombre: {mision.get_nombre()}, "
                                      f"Estado: {mision.get_estado().value}")
                            else:
                                print("No se encontró la misión.")
                        case _:
                            print("Opción inválida.")

                # --- Cambiar estado (funcionalidad exclusiva de Rusia) ---
                case 4:
                    codigo = input("Ingrese el código de la misión: ")
                    self.estacion.cambiar_estado(codigo)

                # --- Mostrar resumen (funcionalidad exclusiva de Rusia) ---
                case 5:
                    self.estacion.mostrar_resumen()

                # --- Iniciar misión (lógica original de EEUU; se reutiliza
                #     buscar_por_codigo(), ya conservado, en vez de repetir el
                #     mismo bucle manual) ---
                case 6:
                    codigo = input("Ingrese el código de la misión a iniciar: ")
                    mision = self.estacion.buscar_por_codigo(codigo)
                    if mision:
                        mision.iniciar()
                    else:
                        print("Misión no encontrada.")

                # --- Finalizar misión (lógica original de EEUU) ---
                case 7:
                    codigo = input("Ingrese el código de la misión a finalizar: ")
                    mision = self.estacion.buscar_por_codigo(codigo)
                    if mision:
                        mision.finalizar()
                    else:
                        print("Misión no encontrada.")

                # --- Salir (lógica original de EEUU, con animación) ---
                case 0:
                    print("Saliendo del sistema", end="", flush=True)
                    for _ in range(3):
                        time.sleep(1)
                        print(".", end="", flush=True)
                    print()
                    break

                case _:
                    print("Opción inválida.")
