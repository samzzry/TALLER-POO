from base_datos import Base_datos
from modelo_vehiculo import Vehiculo
from modelo_vehiculo_deportivo import Vehiculo_deportivo
from modelo_vehiculo_carga import Vehiculo_carga
from modelo_vehiculo_transporte import Vehiculo_transporte


bd = Base_datos()
bd.cargar_datos_iniciales()

while True:
    print("crud vehiculos")
    print("1. agregar vehiculo")
    print("2. eliminar vehiculo")
    print("3. mostrar vehiculos")
    print("4. salir")

    opcion = int(input("seleccione una opcion: "))

    match opcion:
        case 1:
            tipo = input("tipo (normal / deportivo / carga / transporte): ")

            marca = input("marca: ")
            placa = input("placa: ")
            color = input("color: ")

            if tipo == "normal":
                vehiculo = Vehiculo(marca, placa, color)
                bd.agregar_vehiculo(vehiculo)

            elif tipo == "deportivo":
                motor = input("motor: ")
                luces = input("luces: ")
                ventana = input("ventana: ")
                vehiculo = Vehiculo_deportivo(
                    marca, placa, color, motor, luces, ventana
                )
                bd.agregar_vehiculo(vehiculo)

            elif tipo == "carga":
                pasajeros = input("pasajeros: ")
                combustible = input("combustible: ")
                vehiculo = Vehiculo_carga(
                    marca, placa, color, pasajeros, combustible
                )
                bd.agregar_vehiculo(vehiculo)

            elif tipo == "transporte":
                puertas = input("puertas: ")
                llantas = input("llantas: ")
                vehiculo = Vehiculo_transporte(
                    marca, placa, color, puertas, llantas
                )
                bd.agregar_vehiculo(vehiculo)

            else:
                print("tipo no valido")

        case 2:
            posicion = int(input("posicion a eliminar: "))
            bd.eliminar_por_posicion(posicion)

        case 3:
            bd.mostrar_lista()

        case 4:
            break
