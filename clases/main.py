import errores
import parseador
import reporte
import razones

Arjson = parseador.Parser('json/archivoGOLD.json')

cliente = Arjson.cliente #obtengo datos de cliente.
transacciones = Arjson.eventos #obtengo todas las transacciones.
print(cliente.direccion)

#creo un buscador segun las transacciones obtenidas.
# print(buscador.errores) Asi puedo obtener todas las TRANSACCIONES RECHAZADAS.
buscador = errores.Buscador(transacciones)

#obtengo el 'tipo' de operacion de cada transaccion rechazada anteriormente encontrada de un cliente
eventos = buscador.__getTipoTransaccion__()

razon = razones.Razon(eventos, cliente.tipo)
razon.motivo_de_rechazo()

#genero un objeto del html con las razones
html = reporte.GetHTML(cliente, buscador.errores, buscador.sinErrores, razon.razones)

#Ejecuto el html con los datos del cliente.
html.get_html()

