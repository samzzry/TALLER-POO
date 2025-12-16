from modelo_animal import Animal

class Escarabajo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tiene_alas):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tiene_alas = tiene_alas

    def volar(self):
        if self.tiene_alas:
            print(self.nombre, "está volando")
        else:
            print(self.nombre, "no puede volar")

    def enrollarse(self):
        print(self.nombre, "se enrolla para protegerse")

    def mostrar_info(self):
        super().mostrar_info()
        print("Tiene alas:", self.tiene_alas)

