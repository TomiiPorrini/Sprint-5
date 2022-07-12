class Buscador():
    def __init__(self,eventos):
        self.errores = [ x for x in eventos if x['estado']== 'RECHAZADA']

        print(self.errores)