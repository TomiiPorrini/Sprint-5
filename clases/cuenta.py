#creamos los atributos y seteamos sus valores dependiendo del tipo de cliente que sea
class Cuenta():
    def __init__(self, tipoCliente):
        self.tipoCliente = tipoCliente

        if self.tipoCliente == "CLASSIC":
            self.limite_extraccion_diario = 10000
            self.limite_transferencia_recibida = 150000
            self.costo_transferencias = 0.01
        elif self.tipoCliente == "GOLD":
            self.limite_extraccion_diario = 20000
            self.limite_transferencia_recibida = 500000
            self.costo_transferencias = 0.005
        elif self.tipoCliente == "BLACK":
            self.limite_extraccion_diario = 100000
            self.limite_transferencia_recibida = None
            self.costo_transferencias = None

class CuentaCorriente(Cuenta):
    def __init__(self, tipoCliente):
        super().__init__(tipoCliente)
        self.descubierto = -10000

class CajaDeAhorroDolares(Cuenta):
    pass

class CajaDeAhorroPesos(Cuenta):
    pass