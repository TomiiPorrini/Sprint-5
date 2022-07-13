class Cliente:
    def __init__(self,data):
        self.tipo=data['tipo']
        self.dni=data['dni']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        print('Se creo cliente con dni: '+self.dni)
        
    def baja(self):
        self.tipo='baja'

class ClienteClassic(Cliente):
    def __init__(self, data):
        super().__init__(data)
        print('Se creo cliente classic')
        self.tarjeta_debito = True

    def puede_comprar_dolar(self):
        return False

    def puede_crear_chequera(self):
        return False
        
    def puede_crear_tarjeta_credito(self):
        return False

class ClienteGold(Cliente):
    def __init__(self, data):
        super().__init__(data)
        print('Se creo cliente gold')
        self.tarjeta_debito = True
    
    def puede_comprar_dolar(self):
        return True

    def puede_crear_chequera(self):
        return True

    def puede_crear_tarjeta_credito(self):
        return True

class ClienteBlack(Cliente):
    def __init__(self, data):
        super().__init__(data)
        print('Se creo cliente black')
        self.tarjeta_debito = False

    def puede_crear_chequera(self):
        return True

    def puede_crear_tarjeta_credito(self):
        return True

    def puede_comprar_dolar(self):
        return True
