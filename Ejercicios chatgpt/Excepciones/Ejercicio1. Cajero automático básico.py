class FondosInsuficientesError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return self.mensaje


class MontoInsuficienteError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return self.mensaje

class CuentaBancaria:
    def __init__(self):
        self.saldo = 0

    def consultar_saldo(self):
        print(f'Saldo actual: ${self.saldo}')

    def depositar(self, monto):
        if monto>0:
            self.saldo+=monto
            print(f'El deposito ha sido exitoso. Nuevo saldo: ${self.saldo}')
        else:
            raise MontoInsuficienteError('El monto a depositar debe de ser mayor a 0.')

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo-=monto
            print(f'Retiro exitoso. Nuevo saldo: ${self.saldo}')
        elif monto<=0:
            raise FondosInsuficientesError('El monto debe de ser mayor a 0 para poder retirar.')
        else:
            raise FondosInsuficientesError(f'No cuentas con saldo suficiente. Saldo actual: ${self.saldo}')

try:
    cuenta = CuentaBancaria()

    def menu(objeto):
        while True:
            try:
                print('''Indicame que quieres hacer de nuestro menu: 
                         1. Consultar saldo
                         2. Depositar
                         3. Retirar
                         4. Salir''')

                opcion = int(input('Opción: '))

                if opcion == 1:
                    objeto.consultar_saldo()
                elif opcion == 2:
                    monto = int(input('Monto a depositar: '))
                    objeto.depositar(monto)
                elif opcion == 3:
                    monto = int(input('Monto a retirar: '))
                    objeto.retirar(monto)
                elif opcion == 4:
                    break

            except FondosInsuficientesError as e:
                print(e)
            except MontoInsuficienteError as e:
                print(e)


    menu(cuenta)

finally:
    print('Haz salido de la banca.')