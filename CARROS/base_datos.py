class Base_datos:
    def __init__(self):
        self.lista_vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.lista_vehiculos.append(vehiculo)
        print("vehiculo agregado")

    def eliminar_por_posicion(self, posicion):
        if posicion >= 0 and posicion < len(self.lista_vehiculos):
            self.lista_vehiculos.pop(posicion)
            print("vehiculo eliminado")
        else:
            print("posicion no valida")

    def mostrar_lista(self):
        if len(self.lista_vehiculos) == 0:
            print("no hay vehiculos")
        else:
            for i, vehiculo in enumerate(self.lista_vehiculos):
                print("posicion:", i)
                vehiculo.imprimir_info()

    def cargar_datos_iniciales(self):
        from modelo_vehiculo import Vehiculo
        from modelo_vehiculo_deportivo import Vehiculo_deportivo
        from modelo_vehiculo_carga import Vehiculo_carga
        from modelo_vehiculo_transporte import Vehiculo_transporte

        self.lista_vehiculos.append(
            Vehiculo("Toyota", "ABC123", "Blanco")
        )

        self.lista_vehiculos.append(
            Vehiculo_deportivo("Ferrari", "F999", "Rojo", "V8", "LED", "Electricas")
        )

        self.lista_vehiculos.append(
            Vehiculo_carga("Chevrolet", "C456", "Gris", 3, "Diesel")
        )

        self.lista_vehiculos.append(
            Vehiculo_transporte("Mercedes", "T777", "Azul", 4, 6)
        )
