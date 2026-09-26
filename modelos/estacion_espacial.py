from modelos.estado_mision import EstadoMision


# Clase que administra la colección de misiones de la estación.
#
# agregar_mision() y mostrar_misiones(): se conserva la versión del archivo de
# EEUU. agregar_mision() se eligió porque valida que no exista ya una misión
# con el mismo código (funcionalidad de EEUU que Rusia no tenía).
# mostrar_misiones() se eligió porque solo depende de get_codigo/get_nombre/
# get_estado; la versión de Rusia imprimía además destino/duracion/tipo,
# atributos que no existen en la jerarquía de Mision conservada en este proyecto.
#
# buscar_por_codigo(), buscar_por_nombre(), cambiar_estado() y mostrar_resumen():
# son funcionalidad exclusiva del archivo de Rusia, se conservan porque el
# enunciado exige mantener toda funcionalidad exclusiva.
#   - buscar_por_codigo()/buscar_por_nombre() se copian tal cual: solo usan
#     get_codigo()/get_nombre(), compatibles con ambas versiones de Mision.
#   - cambiar_estado(): único ajuste necesario respecto al original: los
#     strings ("Planificada", "En preparación", etc.) se reemplazan por los
#     miembros del Enum EstadoMision, porque ese es el tipo de dato que ya
#     usa set_estado() en este proyecto. Se mantienen las mismas 4 opciones,
#     en el mismo orden y con los mismos mensajes.
#   - mostrar_resumen(): se conserva el conteo de misiones por estado; se
#     retira únicamente la acumulación de "duracion_total", ya que el
#     atributo "duracion" pertenecía solo a la clase MisionEspacial de Rusia
#     y no existe en la jerarquía de Mision conservada (agregarlo violaría la
#     restricción de no crear atributos nuevos).
class EstacionEspacial:
    def __init__(self):
        self.misiones = []

    # --- Exclusivo de EEUU (validación de duplicados) ---
    def agregar_mision(self, mision):
        if any(m.get_codigo() == mision.get_codigo() for m in self.misiones):
            print("⚠️ Ya existe una misión con ese código.")
        else:
            self.misiones.append(mision)
            print("✅ Misión agregada correctamente.")

    # --- Exclusivo de EEUU ---
    def mostrar_misiones(self):
        if not self.misiones:
            print("No hay misiones registradas.")
        else:
            for i, m in enumerate(self.misiones, start=1):
                print(f"{i}. Código: {m.get_codigo()}, Nombre: {m.get_nombre()}, Estado: {m.get_estado().value}")

    # --- Exclusivo de Rusia, sin cambios ---
    def buscar_por_codigo(self, codigo):
        encontrada = None
        for mision in self.misiones:
            if mision.get_codigo() == codigo:
                encontrada = mision
                break
        return encontrada

    # --- Exclusivo de Rusia, sin cambios ---
    def buscar_por_nombre(self, nombre):
        encontrada = None
        for mision in self.misiones:
            if mision.get_nombre().lower() == nombre.lower():
                encontrada = mision
                break
        return encontrada

    # --- Exclusivo de Rusia, adaptado a EstadoMision (Enum) ---
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

    # --- Exclusivo de Rusia; se retira solo la suma de duración (ver nota arriba) ---
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
