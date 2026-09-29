import time

from modelos.estacion_espacial import EstacionEspacial
from modelos.mision_exploracion import MisionExploracion
from modelos.mision_investigacion import MisionInvestigacion
from modelos.mision_rescate import MisionRescate


# Menú principal del programa. Aquí se pueden registrar, buscar y cambiar
# el estado de las misiones.
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
                # Registrar una misión según su tipo.
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

                # Mostrar todas las misiones registradas.
                case 2:
                    self.estacion.mostrar_misiones()

                # Buscar una misión por código o por nombre.
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

                # Cambiar el estado de una misión.
                case 4:
                    codigo = input("Ingrese el código de la misión: ")
                    self.estacion.cambiar_estado(codigo)

                # Mostrar cuántas misiones hay en cada estado.
                case 5:
                    self.estacion.mostrar_resumen()

                # Buscar la misión y luego iniciarla.
                case 6:
                    codigo = input("Ingrese el código de la misión a iniciar: ")
                    mision = self.estacion.buscar_por_codigo(codigo)
                    if mision:
                        mision.iniciar()
                    else:
                        print("Misión no encontrada.")

                # Buscar la misión y luego finalizarla.
                case 7:
                    codigo = input("Ingrese el código de la misión a finalizar: ")
                    mision = self.estacion.buscar_por_codigo(codigo)
                    if mision:
                        mision.finalizar()
                    else:
                        print("Misión no encontrada.")

                # Mostrar unos puntos antes de salir.
                case 0:
                    print("Saliendo del sistema", end="", flush=True)
                    for _ in range(3):
                        time.sleep(1)
                        print(".", end="", flush=True)
                    print()
                    break

                case _:
                    print("Opción inválida.")
