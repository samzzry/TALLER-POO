# clase hija 

from modelo_vehiculo import Vehiculo

class Vehiculo_carga(Vehiculo):
    def __init__(self, marca, placa, color, pasajeros, combustible):
        super().__init__(marca, placa, color)
        self.pasajeros = pasajeros
        self.combustible = combustible

    def contar_pasajeros(self):
        print("la cantidad de pasajeros es:", self.pasajeros)

    def consumir_combustible(self):
        print("el tipo de combustible es:", self.combustible)

    def imprimir_info(self):
        super().imprimir_info()
        print("la cantidad de pasajeros es:", self.pasajeros)
        print("el consumo de combustible es:", self.combustible)
        return "informacion encontrada"
