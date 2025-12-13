from modelo_botella import Botella
class Botella_plastico(Botella):
    def __init__(self, marca, capacidad, tapa, diseno, material, tinte):
        Botella.__init__(self, marca, capacidad, tapa)
        self.diseno = diseno
        self.material = material
        self.tinte = tinte
    def reciclar_botella(self):
        print("la botella se va a reciclar:", self.material)
    def imprimir_info(self):
        print("el diseño es:", self.diseno)
        print("el material es:", self.material)
        print("el color es:", self.tinte)
        Botella.imprimir_info(self)
        print("la tapa padre es:", self.tapa)
        return "informacion encontrada"
