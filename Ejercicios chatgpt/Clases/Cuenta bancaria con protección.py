# Objetivo: Crear una clase CuentaBancaria que oculte el saldo del usuario, permita depositar y retirar dinero y valide los montos con un método privado
class CuentaBancaria:
    def __init__(self, nombre, saldo):
        self.__nombre = nombre
        self.__saldo = saldo

    def ver_saldo(self):
        print(f'Tu saldo es de: {self.__saldo}')

    def depositar(self, monto):
        if self.__monto_valido(monto):
            self.__saldo+=monto

    def retirar(self, monto):
        if monto <= self.__saldo and self.__monto_valido(monto):
            self.__saldo-=monto

    def __monto_valido(self, monto):
        if monto>0:
            return True
        else:
            return None


cuenta = CuentaBancaria("Luis", 1000)

cuenta.ver_saldo()         # Saldo: 1000
saldo1 = float(input('Cuanto es el monto que quieres depositar? '))
cuenta.depositar(saldo1)
cuenta.ver_saldo()         # Saldo: 1500
cuenta.retirar(200)
cuenta.ver_saldo()         # Saldo: 1300
cuenta.depositar(-50)      # No debe depositar nada
cuenta.retirar(2000)       # No debe permitir retirar más de lo disponible
cuenta.ver_saldo()         # Saldo: 1300