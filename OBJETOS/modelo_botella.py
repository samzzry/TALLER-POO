class Botella:
    def __init__(self, marca, capacidad, tapa):
        self.marca = marca
        self.capacidad = capacidad
        self.tapa = tapa
    def llenar_botella(self, capacidad):
        print("la botella se esta llenando:", capacidad)
    def cerrar_tapa(self, cantidad):
        print("se uso la tapa:", self.tapa)
        print("cantidad de tapas usadas:", cantidad)
        return cantidad
    def imprimir_info(self):
        print("la marca es:", self.marca)
        print("el tipo de tapa es:", self.tapa)
        print("la capacidad de la botella es:", self.capacidad)