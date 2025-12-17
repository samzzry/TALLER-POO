from base_datos import Base_datos
from modelo_animal_caballo import Caballo
from modelo_animal_cocodrilo import Cocodrilo
from modelo_animal_escarabajo import Escarabajo
from modelo_animal_pescado import Pescado
from modelo_animal_pato import Pato


bd = Base_datos()
bd.cargar_datos_iniciales()

while True:
    print("crud animales")
    print("1. agregar animal")
    print("2. eliminar animal")
    print("3. mostrar animales")
    print("4. salir")

    opcion = int(input("seleccione una opcion: "))

    match opcion:
        case 1:
            tipo = input("tipo (caballo / cocodrilo / escarabajo / pescado / pato): ")

            nombre = input("nombre: ")
            edad = int(input("edad: "))
            habitat = input("habitat: ")
            dieta = input("dieta: ")
            tamaño = input("tamaño: ")
            color = input("color: ")

            if tipo == "caballo":
                raza = input("raza: ")
                velocidad = int(input("velocidad: "))
                animal = Caballo(
                    nombre, edad, habitat, dieta, tamaño, color, raza, velocidad
                )
                bd.agregar_animal(animal)

            elif tipo == "cocodrilo":
                fuerza = int(input("fuerza de mordida: "))
                animal = Cocodrilo(
                    nombre, edad, habitat, dieta, tamaño, color, fuerza
                )
                bd.agregar_animal(animal)

            elif tipo == "escarabajo":
                alas = input("tiene alas (si/no): ")

                if alas == "si":
                    animal = Escarabajo(
                        nombre, edad, habitat, dieta, tamaño, color, True
                    )
                else:
                    animal = Escarabajo(
                        nombre, edad, habitat, dieta, tamaño, color, False
                    )

                bd.agregar_animal(animal)

            elif tipo == "pescado":
                tipo_agua = input("tipo de agua: ")
                animal = Pescado(
                    nombre, edad, habitat, dieta, tamaño, color, tipo_agua
                )
                bd.agregar_animal(animal)

            elif tipo == "pato":
                pico = input("tipo de pico: ")
                animal = Pato(
                    nombre, edad, habitat, dieta, tamaño, color, pico
                )
                bd.agregar_animal(animal)

            else:
                print("tipo no valido")

        case 2:
            posicion = int(input("posicion a eliminar: "))
            bd.eliminar_por_posicion(posicion)

        case 3:
            bd.mostrar_lista()

        case 4:
            break


