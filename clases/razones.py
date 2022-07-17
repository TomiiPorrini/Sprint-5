class Razon:
    def __init__(self,eventos,tipoCliente):
        self.eventos = eventos
        self.tipoCliente = tipoCliente
        self.razones = []

    def motivo_de_rechazo(self):
        for x in self.eventos:
            if x == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                self.razones.append(RazonRetiroEfectivo(self.eventos,self.tipoCliente).motivo())
            elif x == "ALTA_TARJETA_CREDITO":
                self.razones.append(RazonAltaTarjetaCredito(self.eventos,self.tipoCliente).motivo())
            elif x == "ALTA_CHEQUERA":
                self.razones.append(RazonAltaChequera(self.eventos,self.tipoCliente).motivo())
            elif x == "COMPRA_DOLAR":
                self.razones.append(RazonCompraDolar(self.eventos,self.tipoCliente).motivo())
            elif x == "TRANSFERENCIA_ENVIADA":
                self.razones.append(RazonTransferenciaEnviada(self.eventos,self.tipoCliente).motivo())
            elif x == "TRANSFERENCIA_RECIBIDA":
                self.razones.append(RazonTransferenciaRecibida(self.eventos,self.tipoCliente).motivo())

class RazonAltaChequera(Razon):
    def motivo(self):
        if self.tipoCliente == "CLASSIC":
            return "El tipo de cliente 'CLASSIC' no puede generar chequeras"
        elif self.tipoCliente == "GOLD" or self.tipoCliente == "BLACK":
            return "Supera el limite de chequeras que puede generar por tipo de cliente"

class RazonCompraDolar(Razon):
    def motivo(self):
        if self.tipoCliente == "CLASSIC":
            return "El tipo de cliente 'CLASSIC' no posee caja de ahorro en dolares"
        elif self.tipoCliente == "GOLD" or self.tipoCliente == "BLACK":
            return "No posee saldo suficiente para realizar la compra"

class RazonRetiroEfectivo(Razon):
    def motivo(self):
        return "No posee saldo suficiente para la extraccion o supera el cupo diario restante"

class RazonTransferenciaEnviada(Razon):
    def motivo(self):
        if self.tipoCliente == "CLASSIC" or self.tipoCliente == "GOLD":
            return "No posee saldo suficiente para realizar la tranferencia (tener en cuenta comision por tranferencia)"
        elif self.tipoCliente == "BLACK":
            return "No posee saldo suficiente para realizar la tranferencia"

class RazonTransferenciaRecibida(Razon):
    def motivo(self):
        return "Supera el limite del monto que puede recibir en una tranferencia"

class RazonAltaTarjetaCredito(Razon):
    def motivo(self):
        if self.tipoCliente == "CLASSIC":
            return "El tipo de cliente 'CLASSIC' no puede generarse una tarjeta de credito"
        elif self.tipoCliente == "GOLD" or self.tipoCliente == "BLACK":
            return "Supera el limite de tarjetas de credito que puede generarse por tipo de cliente"
