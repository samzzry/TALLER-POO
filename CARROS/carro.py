class Vehiculo:
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible
    def arranque(self):
        print("el vehiculo ha arrancado")
    def apagado(self):
        print("el vehiculo esta apagado")
    def aceleracion_frenado(self):
        print("puede acelerar y frenar normalmente")
    def sistema_direccion(self):
        print("cuenta con direccion")
    def climatizacion(self):
        print("sistema de aire acondicionado")
    def tipo_seguridad(self):
        print("incluye cinturones y airbags")
    def luces(self):
        print("luces delanteras y traseras")
    def sistema_ventanas(self):
        print("ventanas manuales o electricas ")
    def sistema_espejos(self):
        print("espejos ajustables")S
    def descripcion(self):
        print("vehiculo", self.modelo, "color", self.color, "motor", self.motor)