from clase_animal import animal
class ave(animal):
    def __init__(self, nombre, habitat, dieta, comunicacion):
        animal.__init__(self, nombre, habitat, dieta)
        self.comunicacion = comunicacion
    def info(self):
        print("su manera de comunicarse es por medio de:", self.comunicacion)
        animal.info(self)