# clase padre

class Vehiculo:
    def __init__(self, marca, placa, color):
        self.marca = marca
        self.placa = placa
        self.color = color

    def arrancar_vehiculo(self):
        print("el vehiculo esta arrancando:", self.marca)
        print("con placa:", self.placa)

    def mostrar_color(self):
        print("el vehiculo", self.marca, "tiene color", self.color)

    def aceleracion_frenado(self, velocidad):
        print("el vehiculo", self.marca, "esta acelerando a", velocidad, "km/h")
        print("el vehiculo puede frenar segun la velocidad indicada")

    def imprimir_info(self):
        print("la marca del vehiculo es:", self.marca)
        print("la placa del vehiculo es:", self.placa)
        print("el color del vehiculo es:", self.color)