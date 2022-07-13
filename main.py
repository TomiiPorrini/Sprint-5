import errores
import parseador
import reporte

Arjson = parseador.Parser('json/archivoBLACK.json')


cliente = Arjson.cliente #obtengo datos de cliente.
transacciones = Arjson.eventos #obtengo todas las transacciones.

#creo un buscador segun las transacciones obtenidas.
# print(buscador.errores) Asi puedo obtener todas las TRANSACCIONES RECHAZADAS.
buscador = errores.Buscador(transacciones)

#obtengo el 'tipo' de cada cada transaccion rechazada anteriormente encontrada de un cliente
razones = buscador.__getRazones__()

print("******RAZONES******")
for i, x in enumerate(razones):
    print("Razon", i+1,":", x)
print("******FIN RAZONES******")

#genero un objeto del html con las razones
html = reporte.GetHTML(razones)

#Ejecuto el html con los datos del cliente.
html.get_html()