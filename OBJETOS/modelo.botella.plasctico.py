from modelo_botella import Botella
class Botella_plastico(Botella):
    def _init_(self,marca,capacidad,tapa,diseño,material,tinte):
        super()._init_(marca,capacidad,tapa)
        self.diseño=""
        self.material=""
        self.tinte=""
        def reciclar_botella(self,material):
         self.material 
         print(f"la botella se va a reciclar:{material}")
         def imprimir_info (self):
            print(f" el diseño es:{self.diseño}")
            print(f" el material es:{self:material}")
            print(f" el color es:{self.tinte}")
            super().imprimir_info()
            print(f"la tapa padre es:{super().tapa}")
            return"información Encontrada"