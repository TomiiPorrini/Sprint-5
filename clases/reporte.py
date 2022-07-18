import razones

class GetHTML():
    def __init__(self,cliente, transaccionesRechazadas, transaccionesAceptadas, motivosDeRechazo):
        self.cliente = cliente
        self.transaccionesRec = transaccionesRechazadas
        self.transaccionesAcep = transaccionesAceptadas
        self.motivosDeRechazo = motivosDeRechazo

    def get_html(self):

        #ENCABEZADO DEL HTML
        html = '<html>'
        html += '<head>'
        html += '<meta charset="UTF-8">'
        html += '<meta http-equiv="X-UA-Compatible" content="IE=edge">'
        html += '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        html += '<link rel="stylesheet" href="styles.css" />'
        html += '<title>RESULTADOS DE CLIENTE: {} {}</title>'.format(self.cliente.nombre, self.cliente.apellido)
        html += '</head>' 
        html += '<body>'
        html += '<h1>{}, {}</h1>'.format(self.cliente.nombre, self.cliente.apellido)
        html += '<div>Numero cliente: {}</div>'.format(self.cliente.numero)
        html += '<div>DNI: {}</div>'.format(self.cliente.dni)
        html += '<div>Direccion: {}</div>'.format(self.cliente.direccion)
        
        #TRANSACCIONES RECHAZADAS
        html += '<h1>Transacciones Rechazadas</h1>'
        html += '<table class="table table-striped">'
        html += '<thead>'
        html += '<tr>'
        html += '<th scope="col">Fecha</th>'
        html += '<th scope="col">Tipo</th>'
        html += '<th scope="col">Estado</th>'
        html += '<th scope="col">Monto</th>'
        html += '<th scope="col">Razon</th>'
        html += '</tr>'
        html += '</thead>'
        html += '<body>'
        for i,x in enumerate(self.transaccionesRec):
            html+='<tr>'
            html+='<td>{}</td>'.format(x['fecha'])
            html+='<td>{}</td>'.format(x['tipo'])
            html+='<td>{}</td>'.format(x['estado'])
            html+='<td>{}</td>'.format("$"+x['monto'])
            html+='<td>{}</td>'.format(self.motivosDeRechazo[i])
            html+='</tr>'
        html += '</body>'
        html+='</table>'

        #TRANSACCIONES ACEPTADAS
        html += '<h1>Transacciones Aceptadas</h1>'
        html += '<table class="table table-striped">'
        html += '<thead>'
        html += '<tr>'
        html += '<th scope="col">Fecha</th>'
        html += '<th scope="col">Tipo</th>'
        html += '<th scope="col">Estado</th>'
        html += '<th scope="col">Monto</th>'
        html += '</tr>'
        html += '</thead>'
        html += '<body>'
        for x in self.transaccionesAcep:
            html+='<tr>'
            html+='<td>{}</td>'.format(x['fecha'])
            html+='<td>{}</td>'.format(x['tipo'])
            html+='<td>{}</td>'.format(x['estado'])
            html+='<td>{}</td>'.format("$"+x['monto'])
            html+='</tr>'
        html += '</body>'
        html += '</table>'
        html += '</html>'

        #ESCRITURA Y ENVIO DEL HTML

        self.html = html
        with open("output.html", "w") as text_file:
            text_file.write(self.html)