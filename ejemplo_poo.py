#Programacion orientada a objetos 

class Persona():
    
    def __init__(self, nombre, apellido, edad, meta):
        self.name = nombre
        self.last_name = apellido
        self.__age = edad
        self.meta = meta
    
    def get_pasos(self, pasos):
        if(pasos > self.meta):
            return 'Hoy la rompí haciendo ejercicio'
        else:
            return 'Hoy estuve medio vago'

    def cumple_agnos(self):
        self.__age += 1

    def get_edad(self):
        return f'Hola, me llamo {self.name} {self.last_name} y tengo {self.__age} años'
    
persona1 = Persona("Mauricio", "Cuello", 30, 10000)
persona2 = Persona("Lionel", "Messi", 34, 500)

print(persona2.get_pasos(800))
