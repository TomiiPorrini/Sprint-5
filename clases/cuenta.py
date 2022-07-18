#los clientes tipo GOLD y BLACK tienen esta cuenta con un determinado descubierto segun consigna
class CuentaCorriente():
    def __init__(self):
        self.descubierto = -10000

#con esta cuenta se puede comprar dolares segun consigna
class CajaDeAhorroDolares():
    def __init__(self):
        self.puedeComprarDolares = True

#creamos los atributos y seteamos sus valores dependiendo del tipo de cliente que sea
class CajaDeAhorroPesos():
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