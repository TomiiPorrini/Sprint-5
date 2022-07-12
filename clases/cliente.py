class Cliente:
    def __init__(self,data, direccion):
        self.tipo=data['tipo']
        self.dni=data['dni']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.direccion = direccion
        print('Se creo cliente: '+self.dni)
        
    def baja(self):
        self.tipo='baja'

class ClienteClassic(Cliente):
    def __init__(self, data):
        print('Se creo classic')
        self.tarjeta_debito = True
        super().__init__(data)

    def puede_comprar_dolar(self):
        return False

    def puede_crear_chequera():
        return False
        
    def puede_crear_tarjeta_credito():
        return False

class ClienteGold(Cliente):
    def __init__(self, data):
        print('Se creo gold')
        self.tarjeta_debito = True
        super().__init__(data)
    
    def puede_comprar_dolar(self):
        return True

    def puede_crear_chequera():
        return True

    def puede_crear_tarjeta_credito():
        return True

class ClienteBlack(Cliente):
    def __init__(self, data):
        print('Se creo black')
        self.tarjeta_debito = False
        super().__init__(data)

    def puede_crear_chequera():
        return True

    def puede_crear_tarjeta_credito():
        return True

    def puede_comprar_dolar(self):
        return True
