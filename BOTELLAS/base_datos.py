class Base_datos:
    def __init__(self):
        self.lista_botellas = []

    def agregar_botella(self, botella):
        self.lista_botellas.append(botella)
        print("botella agregada")

    def eliminar_por_posicion(self, posicion):
        self.lista_botellas.pop(posicion)
        print("botella eliminada")

    def mostrar_lista(self):
        if len(self.lista_botellas) == 0:
            print("no hay botellas")
        else:
            for i, botella in enumerate(self.lista_botellas):
                print("posicion:", i)
                botella.imprimir_info()

    def cargar_datos_iniciales(self):
        from modelo_botella import Botella
        from modelo_botella_plastico import Botella_plastico
        from modelo_botella_vidrio import Botella_vidrio

        self.lista_botellas.append(Botella("coca_cola", "1.5l", "especial"))
        self.lista_botellas.append(
            Botella_plastico("pepsi", "2.5l", "comun", "redondo", "plastico", "sin tinte")
        )
        self.lista_botellas.append(
            Botella_vidrio("kola roman", "1.5l", "comun", "cubo", "vidrio", "roja")
        )
