from modelo_vehiculo import Vehiculo
from modelo_vehiculo_deportivo import Vehiculo_deportivo
from modelo_vehiculo_carga import Vehiculo_carga
from modelo_vehiculo_transporte import Vehiculo_transporte


vehiculo = Vehiculo("Ferrari", "MN678", "Negro")
vehiculo.imprimir_info()


deportivo = Vehiculo_deportivo("Lamborghini", "GTX987", "Rojo", "V12 6.5L", "LED", "Electricas")
print(deportivo.imprimir_info())


carga = Vehiculo_carga("Chevrolet NHR", "TR909", "Blanco", 3, "Diesel")
print(carga.imprimir_info())


transporte = Vehiculo_transporte("Mercedes Benz", "GT500", "Azul", 4, 6)
print(transporte.imprimir_info())
