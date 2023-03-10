from fcntl import F_SEAL_SEAL
import direccion
import cuenta

class Cliente:
    def __init__(self,data):
        self.tipo = data['tipo']
        self.dni = data['dni']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.numero = data['numero']
        self.direccion = direccion.Direccion(data['direccion'])
        print('Se creo cliente con dni: '+self.dni)
        
class ClienteClassic(Cliente):
    def __init__(self, data):
        super().__init__(data)
        print('Se creo cliente classic')
        self.tarjeta_debito = True
        self.cajaDeAhorroEnPesos = cuenta.CajaDeAhorroPesos(self.tipo)
        self.cuentaCorriente = None
        self.cajaDeAhorroEnDolares = None

    def puede_comprar_dolares(self):
        if self.cajaDeAhorroEnDolares != None:
            return True
        else:
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
        self.cajaDeAhorroEnPesos = cuenta.CajaDeAhorroPesos(self.tipo)
        self.cuentaCorriente = cuenta.CuentaCorriente()
        self.cajaDeAhorroEnDolares = cuenta.CajaDeAhorroDolares()

    def puede_comprar_dolares(self):
        if self.cajaDeAhorroEnDolares != None:
            return True
        else:
            return False

    def puede_crear_chequera(self):
        return True

    def puede_crear_tarjeta_credito(self):
        return True

class ClienteBlack(Cliente):
    def __init__(self, data):
        super().__init__(data)
        print('Se creo cliente black')
        self.tarjeta_debito = False
        self.cajaDeAhorroEnPesos = cuenta.CajaDeAhorroPesos(self.tipo)
        self.cuentaCorriente = cuenta.CuentaCorriente()
        self.cajaDeAhorroEnDolares = cuenta.CajaDeAhorroDolares()

    def puede_comprar_dolares(self):
        if self.cajaDeAhorroEnDolares != None:
            return True
        else:
            return False
    
    def puede_crear_chequera(self):
        return True

    def puede_crear_tarjeta_credito(self):
        return True

