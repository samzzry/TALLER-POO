from carro import Vehiculo
class CamionetaCarga(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible, capacidad_carga_kg):
        Vehiculo.__init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.capacidad_carga_kg = capacidad_carga_kg
    def climatizacion(self):
        print("climatizacion basica para cabina de trabajo")
    def info_extra(self):
        print("capacidad de carga:", self.capacidad_carga_kg, "kg")
