class ErrorRetiroDeposito(Exception):
    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f'{self.mensaje}, {self.codigo}.'

class CuentaBancaria:
    def __init__(self, id, nombre, apertura):
        self.dinero_disponible = apertura

    def deposito(self, saldo):
        if saldo<0:
            raise ErrorRetiroDeposito('La cantidad a depositar no puede ser negativa.', 400)
        self.dinero_disponible+=saldo
        print(f'Deposito exitoso. Nuevo saldo: ${self.dinero_disponible}')

    def retiro(self, saldo):
        if saldo<0:
            raise ErrorRetiroDeposito('La cantidad a retirar no puede ser negativa', 400)
        elif saldo>self.dinero_disponible:
            raise ErrorRetiroDeposito('Fondos insuficientes para realizar retiro', 401)
        self.dinero_disponible-=saldo
        print(f'Retiro exitoso. Nuevo saldo: ${self.dinero_disponible}')

    def consultar_saldo(self):
        print(f'Tu dinero disponible es: ${self.dinero_disponible}')

try:
    cuenta = CuentaBancaria("123456789", "Juan Perez", 1000)
    cuenta.consultar_saldo()
    cuenta.deposito(500)
    cuenta.retiro(2000)
except ErrorRetiroDeposito as e:
    print(e)

try:
    cuenta.retiro(-100)

except ErrorRetiroDeposito as e:
    print(e)