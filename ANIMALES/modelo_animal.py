

class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    def moverse(self):
        print(self.nombre, "se está moviendo")

    def comunicarse(self):
        print(self.nombre, "se está comunicando")

    def reproducirse(self):
        print(self.nombre, "se está reproduciendo")

    def alimentarse(self):
        print(self.nombre, "se alimenta de", self.dieta)

    def adaptarse(self):
        print(self.nombre, "se está adaptando a", self.habitat)

    def instinto(self):
        print(self.nombre, "actúa por instinto")

    def descansar(self):
        print(self.nombre, "está descansando")

    def sueño(self):
        print(self.nombre, "está durmiendo")

    def interaccion_social(self):
        print(self.nombre, "interactúa socialmente")

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Hábitat:", self.habitat)
        print("Dieta:", self.dieta)
        print("Tamaño:", self.tamaño)
        print("Color:", self.color)
