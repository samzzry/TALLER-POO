from modelo_animal import Animal

class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, raza, velocidad):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.raza = raza
        self.velocidad = velocidad

    def galopar(self):
        print(self.nombre, "está corriendo")

    def relinchar(self):
        print(self.nombre, "está relinchando")

    def mostrar_info(self):
        super().mostrar_info()
        print("Raza:", self.raza)
        print("Velocidad:", self.velocidad)
