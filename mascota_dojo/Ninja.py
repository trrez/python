import Mascota


class Ninja:
    def __init__(self, nombre, apellido, mascota, premio, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = Mascota.Mascota(mascota, "tipo_mascota", "golosina")
        self.premio = premio
        self.comida_mascota = comida_mascota

    def caminar(self):
        self.mascota.jugar()

    def alimentar(self):
        self.mascota.comer()

    def banar(self):
        self.mascota.ruido()


ninja = Ninja("Tatiana", "Gutierrez", "Leon",
              "Juguete", "Carne")
ninja.caminar()
ninja.alimentar()
ninja.banar()
