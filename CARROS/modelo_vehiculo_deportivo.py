# clase hija 

from modelo_vehiculo import Vehiculo

class Vehiculo_deportivo(Vehiculo):
    def __init__(self, marca, placa, color, motor, luces, ventana):
        super().__init__(marca, placa, color)
        self.motor = motor
        self.luces = luces
        self.ventana = ventana

    def prender_motor(self):
        print("el tipo de motor es:", self.motor)

    def ver_luces(self):
        print("las luces del vehiculo deportivo son", self.luces)

    def sistema_ventanas(self):
        print("las ventanas del vehiculo deportivo son", self.ventana)

    def imprimir_info(self):
        super().imprimir_info()
        print("El motor es:", self.motor)
        print("Las luces son:", self.luces)
        print("Las ventanas son:", self.ventana)
        return "Informacion encontrada"
