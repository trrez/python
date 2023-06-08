class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.balance_cuenta = 1000

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: {self.balance_cuenta}")

    def transfer_dinero(self, other_user, amount):
        self.other_user = other_user
        other_user.balance_cuenta += amount
        self.balance_cuenta -= amount


usr1 = User('Tatiana', 'tatiana@gmail.com')
usr2 = User('copito', 'copito@gmail.com')
usr3 = User('Medusa', 'medusa@gmail.com')
usr1.mostrar_balance_usuario()
usr2.mostrar_balance_usuario()
usr3.mostrar_balance_usuario()
usr1.hacer_deposito(200)
usr1.hacer_deposito(100)
usr1.hacer_deposito(300)
usr1.hacer_retiro(300)
usr2.hacer_deposito(100)
usr2.hacer_deposito(100)
usr2.hacer_retiro(300)
usr2.hacer_retiro(600)
usr3.hacer_deposito(700)
usr3.hacer_retiro(300)
usr3.hacer_retiro(600)
usr3.hacer_retiro(600)
usr1.transfer_dinero(usr3, 200)
usr1.mostrar_balance_usuario()
usr2.mostrar_balance_usuario()
usr3.mostrar_balance_usuario()
