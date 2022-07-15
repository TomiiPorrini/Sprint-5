import errores
import parseador
import reporte

Arjson = parseador.Parser('json/archivoBLACK.json')

cliente = Arjson.cliente #obtengo datos de cliente.
transacciones = Arjson.eventos #obtengo todas las transacciones.
print(cliente.direccion)

#creo un buscador segun las transacciones obtenidas.
# print(buscador.errores) Asi puedo obtener todas las TRANSACCIONES RECHAZADAS.
buscador = errores.Buscador(transacciones)

#obtengo el 'tipo' de cada cada transaccion rechazada anteriormente encontrada de un cliente
# razones = buscador.__getRazones__()


#genero un objeto del html con las razones
html = reporte.GetHTML(cliente, buscador.errores, buscador.sinErrores)

#Ejecuto el html con los datos del cliente.
html.get_html()

