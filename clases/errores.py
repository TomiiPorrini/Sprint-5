class Buscador():
    def __init__(self,eventos):
        self.errores = [x for x in eventos if x['estado'] == 'RECHAZADA']
        self.sinErrores = [x for x in eventos if x['estado'] == 'ACEPTADA']
        
    def __getRazones__(self):
        self.razones = [x['tipo'] for x in self.errores]
        return self.razones