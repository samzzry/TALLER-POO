from modelo_animal_caballo import Caballo
from modelo_animal_cocodrilo import Cocodrilo
from modelo_animal_escarabajo import Escarabajo
from modelo_animal_pescado import Pescado
from modelo_animal_pato import Pato

caballo = Caballo("Spirit", 5, "Pradera", "Hierba", "Grande", "Marrón", "Mustang", 60)
caballo.mostrar_info()
caballo.galopar()
caballo.alimentarse()
print()

cocodrilo = Cocodrilo("Coco", 12, "Pantano", "Carnívoro", "Grande", "Verde", 3000)
cocodrilo.mostrar_info()
cocodrilo.atacar()
cocodrilo.nadar()
print()

escarabajo = Escarabajo("Bicho", 1, "Bosque", "Hojas", "Pequeño", "Negro", True)
escarabajo.mostrar_info()
escarabajo.volar()
print()

pescado = Pescado("Nemo", 2, "Arrecife", "Plancton", "Pequeño", "Naranja", "Salada")
pescado.mostrar_info()
pescado.nadar()
print()

pato = Pato("Donald", 3, "Lago", "Omnívoro", "Mediano", "Blanco", "Ancho")
pato.mostrar_info()
pato.graznar()
