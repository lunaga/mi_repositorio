# perro = Perro('Canino', 4, 'Jaime')

# perro.describeme()
# perro.ladrar()
# perro.hablar()
# perro.moverse()

# class Factura:
#     def costo(self):
#         #precio * cantidad
#         pass

# class FacturaConDescuento(Factura):
#     def costo(self):
#         #super().costo() - descuento
#         pass


class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        print('Ojota, voy a hablar...')

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un animal del tipo", type(self).__name__)












class Perro(Animal):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad)
        self.nombre = nombre
    
    def ladrar(self):
        print('Guau')

    def hablar(self):
        super().hablar()
        print(self.nombre + ': Wau wau')

class Abeja(Animal):
    def hablar(self):
        print('Bzzzzz')

    def picar(self):
        print('OUCH!')

animal = Animal('Mamífero', 20)

animal.describeme()
animal.hablar()
animal.moverse()

perro = Perro('Canino', 4
