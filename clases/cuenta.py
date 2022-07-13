class Cuenta():
    def __init__(self, extDia, TransfRec, monto, transferencia, descubierto):
        self.limite_extraccion_diario = extDia
        self.limite_transferencia_recibida = TransfRec
        self.monto = monto
        self.costo_transferencias = transferencia
        self.saldo_descubierto_disponible = descubierto
    
class CuentaCorriente():
    pass
class CajaDeAhorroDolares():
    pass
class CajaDeAhorroPesos():
    pass