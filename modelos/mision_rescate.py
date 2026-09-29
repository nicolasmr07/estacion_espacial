from modelos.mision import Mision
from modelos.estado_mision import EstadoMision


# Misión de rescate, con la tripulación que se va a rescatar.
class MisionRescate(Mision):
    def __init__(self, codigo, nombre, tripulacion):
        super().__init__(codigo, nombre)
        self.tripulacion = tripulacion

    def iniciar(self):
        if self.get_estado() == EstadoMision.PLANIFICADA:
            self.set_estado(EstadoMision.EJECUCION)
            print(f"🆘 Rescate en curso de {self.tripulacion}: {self.get_nombre()}")
        else:
            print("⚠️ No se puede iniciar esta misión.")

    def finalizar(self):
        if self.get_estado() == EstadoMision.EJECUCION:
            self.set_estado(EstadoMision.FINALIZADA)
            print(f"🙌 Rescate completado de {self.tripulacion}: {self.get_nombre()}")
        else:
            print("⚠️ No se puede finalizar esta misión.")
