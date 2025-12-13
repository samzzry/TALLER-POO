from clase_animal import animal
class reptil(animal):
    def __init__(self, nombre, habitat, dieta, moverse):
        animal.__init__(self, nombre, habitat, dieta)
        self.moverse = moverse
    def info(self):
        print("se mueve de forma:", self.moverse, "para cazar en el agua")
        animal.info(self)