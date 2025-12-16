from modelo_animal import Animal

class Pescado(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_agua):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_agua = tipo_agua

    def nadar(self):
        print(self.nombre, "está nadando")

    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo de agua:", self.tipo_agua)
