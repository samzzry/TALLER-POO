from clase_animal import animal
class terrestre(animal):
    def __init__(self, nombre, habitat, dieta, color):
        animal.__init__(self, nombre, habitat, dieta)
        self.color = color
    def info(self):
        print("su pelaje es:", self.color)
        animal.info(self)