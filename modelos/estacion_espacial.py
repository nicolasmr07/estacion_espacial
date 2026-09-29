from modelos.estado_mision import EstadoMision


# Guarda y administra las misiones registradas en la estación.
class EstacionEspacial:
    def __init__(self):
        self.misiones = []

    # Evita registrar dos misiones con el mismo código.
    def agregar_mision(self, mision):
        if any(m.get_codigo() == mision.get_codigo() for m in self.misiones):
            print("⚠️ Ya existe una misión con ese código.")
        else:
            self.misiones.append(mision)
            print("✅ Misión agregada correctamente.")

    def mostrar_misiones(self):
        if not self.misiones:
            print("No hay misiones registradas.")
        else:
            for i, m in enumerate(self.misiones, start=1):
                print(f"{i}. Código: {m.get_codigo()}, Nombre: {m.get_nombre()}, Estado: {m.get_estado().value}")

    def buscar_por_codigo(self, codigo):
        encontrada = None
        for mision in self.misiones:
            if mision.get_codigo() == codigo:
                encontrada = mision
                break
        return encontrada

    def buscar_por_nombre(self, nombre):
        encontrada = None
        for mision in self.misiones:
            if mision.get_nombre().lower() == nombre.lower():
                encontrada = mision
                break
        return encontrada

    def cambiar_estado(self, codigo):
        mision = self.buscar_por_codigo(codigo)
        if mision is None:
            print("No se encontró la misión.")
            return

        print("\nSeleccione el nuevo estado:")
        print("1. Planificada")
        print("2. En preparación")
        print("3. En ejecución")
        print("4. Finalizada")

        opcion = input("Seleccione una opción: ")
        if not opcion.isdigit():
            print("Debe ingresar un número.")
            return

        match int(opcion):
            case 1:
                mision.set_estado(EstadoMision.PLANIFICADA)
                print("Estado actualizado.")
            case 2:
                mision.set_estado(EstadoMision.PREPARACION)
                print("Estado actualizado.")
            case 3:
                mision.set_estado(EstadoMision.EJECUCION)
                print("Estado actualizado.")
            case 4:
                mision.set_estado(EstadoMision.FINALIZADA)
                print("Estado actualizado.")
            case _:
                print("Opción inválida.")

    def mostrar_resumen(self):
        total = 0
        planificadas = 0
        preparacion = 0
        ejecucion = 0
        finalizadas = 0

        for mision in self.misiones:
            total = total + 1
            if mision.get_estado() == EstadoMision.PLANIFICADA:
                planificadas = planificadas + 1
            elif mision.get_estado() == EstadoMision.PREPARACION:
                preparacion = preparacion + 1
            elif mision.get_estado() == EstadoMision.EJECUCION:
                ejecucion = ejecucion + 1
            elif mision.get_estado() == EstadoMision.FINALIZADA:
                finalizadas = finalizadas + 1

        print("\n============== RESUMEN ==============")
        print(f"Total de misiones: {total}")
        print(f"Planificadas: {planificadas}")
        print(f"En preparación: {preparacion}")
        print(f"En ejecución: {ejecucion}")
        print(f"Finalizadas: {finalizadas}")
        print("======================================")
