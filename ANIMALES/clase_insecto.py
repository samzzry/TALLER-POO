from clase_animal import animal
class insecto(animal):
    def __init__(self, nombre, habitat, dieta, reproduccion):
        animal.__init__(self, nombre, habitat, dieta)
        self.reproduccion = reproduccion
    def info(self):
        print("su reproduccion es:", self.reproduccion)
        animal.info(self)