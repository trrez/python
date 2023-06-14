class Mascota:
    salud = 0
    energia = 0

    def __init__(self, name, tipo, golosina):
        self.name = name
        self.tipo = tipo
        self.golosina = golosina

    def dormir(self):
        self.energia += 25
        print(f"{self.name} is sleeping")
        print(f"Energia: {self.energia}")

    def comer(self):
        self.energia += 5
        self.salud += 10
        print(f"feeding {self.name} {self.golosina}")
        print(f"Salud: {self.salud}")
        print(f"Energia: {self.energia}")
        return self.energia

    def jugar(self):
        self.salud += 5
        print(f"playing with {self.name}")
        print(f"Salud: {self.salud}")

    def ruido(self):
        print(f"{self.name} says RAWW")
