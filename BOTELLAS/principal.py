from base_datos import Base_datos
from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico
from modelo_botella_vidrio import Botella_vidrio


bd = Base_datos()
bd.cargar_datos_iniciales()

while True:
    print("crud botellas")
    print("1. agregar botella")
    print("2. eliminar botella")
    print("3. mostrar botellas")
    print("4. salir")

    opcion = int(input("seleccione una opcion: "))

    match opcion:
        case 1:
            tipo = input("tipo (normal / plastico / vidrio): ")

            marca = input("marca: ")
            capacidad = input("capacidad: ")
            tapa = input("tapa: ")

            if tipo == "normal":
                botella = Botella(marca, capacidad, tapa)

            elif tipo == "plastico":
                diseño = input("diseño: ")
                material = input("material: ")
                tinte = input("tinte: ")
                botella = Botella_plastico(marca, capacidad, tapa, diseño, material, tinte)

            elif tipo == "vidrio":
                diseño = input("diseño: ")
                material = input("material: ")
                tinte = input("tinte: ")
                botella = Botella_vidrio(marca, capacidad, tapa, diseño, material, tinte)

            bd.agregar_botella(botella)

        case 2:
            posicion = int(input("posicion a eliminar: "))
            bd.eliminar_por_posicion(posicion)

        case 3:
            bd.mostrar_lista()

        case 4:
            break