from modelos.mision import Mision
from modelos.estado_mision import EstadoMision


# Misión de investigación. Primero pasa por preparación y luego entra en
# ejecución.
class MisionInvestigacion(Mision):
    def __init__(self, codigo, nombre, area):
        super().__init__(codigo, nombre)
        self.area = area

    def iniciar(self):
        if self.get_estado() == EstadoMision.PLANIFICADA:
            self.set_estado(EstadoMision.PREPARACION)
            print(f"🛰️ Preparando investigación en {self.area}: {self.get_nombre()}")
        elif self.get_estado() == EstadoMision.PREPARACION:
            self.set_estado(EstadoMision.EJECUCION)
            print(f"🔬 Investigación en ejecución en {self.area}: {self.get_nombre()}")
        else:
            print("⚠️ No se puede iniciar esta misión.")

    def finalizar(self):
        if self.get_estado() == EstadoMision.EJECUCION:
            self.set_estado(EstadoMision.FINALIZADA)
            print(f"✅ Investigación finalizada en {self.area}: {self.get_nombre()}")
        else:
            print("⚠️ No se puede finalizar esta misión.")
