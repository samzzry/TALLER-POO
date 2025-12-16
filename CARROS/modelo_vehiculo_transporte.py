# Clase hija Vehiculo_transporte

from modelo_vehiculo import Vehiculo

class Vehiculo_transporte(Vehiculo):
    def __init__(self, marca, placa, color, puertas, llantas):
        super().__init__(marca, placa, color)
        self.puertas = puertas
        self.llantas = llantas

    def usar_puertas(self):
        print("el vehiculo tiene", self.puertas, "puertas")

    def tener_llantas(self):
        print("el vehiculo tiene", self.llantas, "llantas")

    def imprimir_info(self):
        super().imprimir_info()
        print("las puertas son:", self.puertas)
        print("las llantas son:", self.llantas)
        return "informacion encontrada"
