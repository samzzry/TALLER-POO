from clase_animal import animal
class acuatico(animal):
    def __init__(self, nombre, habitat, dieta, instintos):
        animal.__init__(self, nombre, habitat, dieta)
        self.instintos = instintos
    def info(self):
        print("este animal tiene instintos:", self.instintos)
        animal.info(self)