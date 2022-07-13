class Direccion():
    def __init__(self, calle, numero, ciudad, provincia, pais):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais
    
    def __str__(self):
        return 'Domicilio: calle: {} N°{}, {}, {}, {}'.format(self.calle, self.numero, self.ciudad, self.provincia, self.pais)