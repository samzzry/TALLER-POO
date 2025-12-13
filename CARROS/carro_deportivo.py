from carro import Vehiculo
class CarroDeportivo(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        Vehiculo.__init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.modo_sport = True
    def aceleracion_frenado(self):
        print("aceleracion rapida y frenado deportivo")
    def info_extra(self):

        print("modo sport activo:", self.modo_sport)
