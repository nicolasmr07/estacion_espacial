from modelos.mision import Mision
from modelos.estado_mision import EstadoMision


# Misión de exploración en un planeta.
class MisionExploracion(Mision):
    def __init__(self, codigo, nombre, planeta):
        super().__init__(codigo, nombre)
        self.planeta = planeta

    def iniciar(self):
        if self.get_estado() == EstadoMision.PLANIFICADA:
            self.set_estado(EstadoMision.EJECUCION)
            print(f"🚀 Exploración iniciada en {self.planeta}: {self.get_nombre()}")
        else:
            print("⚠️ No se puede iniciar esta misión.")

    def finalizar(self):
        if self.get_estado() == EstadoMision.EJECUCION:
            self.set_estado(EstadoMision.FINALIZADA)
            print(f"🌌 Exploración finalizada en {self.planeta}: {self.get_nombre()}")
        else:
            print("⚠️ No se puede finalizar esta misión.")
