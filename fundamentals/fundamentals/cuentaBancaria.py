class CuentaBancaria:
    cuentas = []

    def __init__(self, tasa_interes=1.01, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        print(f"Balance: {self.balance}")
        return self

    def retiro(self, amount):
        if self.balance < 0:
            print(f"Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= -5
        else:
            self.balance -= amount
            print(f"Balance: {self.balance}")
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")
        return self

    def generar_interes(self):
        self.balance = self.balance * self.tasa_interes
        print(f"Balance: {self.balance}")
        return self

    @classmethod
    def imprimir_todas_las_cuentas(cls):
        for cuenta in cls.cuentas:
            print("------")
            cuenta.mostrar_info_cuenta()


usr1 = CuentaBancaria()
usr2 = CuentaBancaria()
usr1.deposito(200).deposito(200).deposito(100).retiro(200).generar_interes()
usr2.deposito(600).deposito(500).retiro(100).retiro(
    200).retiro(200).retiro(100).generar_interes()
CuentaBancaria.imprimir_todas_las_cuentas()
