class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.balance_cuenta = 1000

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        return self

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
        return self

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: {self.balance_cuenta}")

    def transfer_dinero(self, other_user, amount):
        self.other_user = other_user
        other_user.balance_cuenta += amount
        self.balance_cuenta -= amount
        return self


usr1 = User('Tatiana', 'tatiana@gmail.com')
usr2 = User('copito', 'copito@gmail.com')
usr3 = User('Medusa', 'medusa@gmail.com')
usr1.mostrar_balance_usuario()
usr2.mostrar_balance_usuario()
usr3.mostrar_balance_usuario()
usr1.hacer_deposito(200).hacer_deposito(100).hacer_deposito(
    300).hacer_retiro(300).transfer_dinero(usr3, 200).mostrar_balance_usuario()
usr2.hacer_deposito(100).hacer_deposito(
    100).hacer_retiro(300).hacer_retiro(600).mostrar_balance_usuario()
usr3.hacer_deposito(700).hacer_retiro(300).hacer_retiro(
    600).hacer_retiro(600).mostrar_balance_usuario()
