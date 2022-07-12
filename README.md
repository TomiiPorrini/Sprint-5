# Consigna Final Sprint 5 - Segmentación de clientes

ITBANK tiene distintos tipos de clientes y distintos tipos de cuentas que le puede dar
a cada uno. A continuación se detallan las características de cada uno de ellos
## Tipos de clientes
* Classic
* Gold
* Black
## Tipos de cuentas
* Caja de ahorro en pesos
* Caja de ahorro en dólares
* Cuenta Corriente
Adicionalmente los clientes pueden tener distintos tipos de tarjetas de crédito y
operaciones permitidas según su perfil asociado.
## Ejemplo
* Clientes Classic
* Tiene solamente una tarjeta de débito que se crea junto con el cliente.
* Solo tiene una caja ahorro en pesos creada cuando se dio de alta el cliente.
Como no tiene cuenta en dólares, no puede comprar y vender dólares.
* Solo se le permite retirar hasta un máximo de $10.000 diarios por cajero.
* No tienen acceso a tarjetas de crédito ni chequeras
* La comisión por transferencias hechas es de 1%.
* No puede recibir transferencias mayores a $150.000 sin previo aviso.
* Clientes Gold
* Tiene una tarjeta de débito que se crea con el cliente.
* Tiene una cuenta corriente con un descubierto de $10.000. Hay que tener
presente que como tiene cuenta corriente el saldo en la cuenta podría ser
negativo y hasta -$10.000 si tiene cupo diario para la operación que se
quiera realizar.
* Tiene una caja de ahorro en dólares, por lo que puede comprar dólares.
* Puede tener solo una tarjeta de crédito.
* Las extracciones de efectivo tienen un máximo de $20.000 por día.
* Pueden tener una chequera.
* La comisión por transferencias hechas es de 0,5%.
* No puede recibir transferencias mayores a $500.000 sin previo aviso.
* Clientes Black
* Los clientes Black tienen una caja de ahorro en pesos, cuenta corriente en
pesos, y una caja de ahorro en dólares.
* Pueden tener un descubierto en su cuenta corriente de hasta $10.000.
* Pueden tener hasta 5 tarjetas de crédito.
* Pueden extraer hasta $100.000 por día
* Pueden tener hasta dos chequeras.
* No se aplican comisiones a las transferencias.
* Pueden recibir transferencias por cualquier monto sin previa autorización
## Problemática
El banco cuenta con un sistema TPS (Sistema de Procesamiento de Transacciones)
que tiene como principal función enviar las transacciones ocurridas, diferenciando
si fueron aceptadas o no (sin indicar la razón). Dicho sistema tiene años de
funcionamiento en el banco y fue depurado varias veces, llevando la tasa de
errores al mínimo, por lo que se sabe que funciona correctamente. El equipo de TI,
identifica este sistema como un "Legacy" o "Legado". La única salida que provee el
sistema, son los datos "crudos" del evento ocurrido con los montos asociados sin
ningún procesamiento o información adicional.
El área de operaciones del banco está integrada por gente de mucha experiencia
en el banco que utiliza planillas propias para poder procesar la salida de datos del
TPS. Dado que actualmente ITBANK se encuentra en un proceso de renovación, se
están incorporando nuevos empleados al área de referencia. Es por ese motivo que
el gerente requiere una automatización del procesamiento de los datos emitidos
por el TPS. La mejor forma de abordar este problema es generar una aplicación
que reciba como input la información del TPS, la procese y emita un reporte que 
sea capaz de mostrar la razón de porque estas transacciones fueron rechazadas
para ponerla a disposición del equipo de atención al cliente. Si son aceptadas
simplemente se agrega al reporte la transacción que se hizo sin detalle particular,
de esta forma quedara completo el informe.
En el reporte se debe incluir el nombre de cliente, número, DNI, dirección y para
cada transacción la fecha , el tipo de operación, el estado, el monto y razón por la
cual se rechazó (vacío en caso de ser aceptada).
Se pide que el reporte sea una página en HTML válida de forma que el browser
estándar del banco lo pueda interpretar y visualizar.
La salida del sistema TPS es un archivo JSON con las transacciones que debemos
procesar.
* Ejemplo
{
 "numero": 100001,
 "nombre": "Nicolas",
 "apellido": "Gastón",
 "DNI": "29494777",
 "tipo": "BLACK",
 "transacciones": [
 {
 "estado": "ACEPTADA",
 "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
 "cuentaNumero": 190,
 "cupoDiarioRestante": 9000,
 "monto": 1000,
 "fecha": "10/10/2022 16: 00: 55",
 "numero": 1,
 "saldoEnCuenta": 100000,
 "totalTarjetasDeCreditoActualmente" : 5,
 "totalChequerasActualmente" : 2
 },
 {
 "estado": "RECHAZADA",
 "tipo": "ALTA_CHEQUERA",
 "cuentaNumero": 190,
 "cupoDiarioRestante": 3000,
 "monto": 9000,
 "fecha": "10/10/2022 16:00:55",
 "numero": 1,
 "saldoEnCuenta": 100000,
 "totalTarjetasDeCreditoActualmente" : 5,
 "totalChequerasActualmente" : 2
 }
 ]
}
NOTA: Se adjuntan ejemplos para cada tipo de cliente de eventos aceptados y
rechazados.

## Las transacciones que informa el sistema legado son acotadas. Actualmente informa las siguientes transacciones:

* RETIRO_EFECTIVO_CAJERO_AUTOMATICO: Tener presente que si tiene
cuenta corriente puede figurar el valor de saldo en cuenta como negativo
hasta el importe del cupo establecido
* ALTA_TARJETA_CREDITO: Se solicito una nueva tarjeta de crédito
* ALTA_CHEQUERA: Se solicito una nueva chequera
* COMPRAR_DOLAR: Se solicito realizar la transacción para comprar
dólares, pero solo lo pueden hacer los clientes que tengan cuenta en
dólares.
* TRANSFERENCIA_ENVIADA: Solo se puede en pesos y lo que tenga en caja
de ahorro y cuenta corriente debe poder pagar la comisión que se cobra.
* TRANSFERENCIA_RECIBIDA: Sólo en pesos y tener presente que va a estar
rechaza si no estuvo autorizada.
## Restricciones
El equipo de arquitectura de TI del ITBANK estableció los siguientes principios:
* Se debe utilizar programación orientada a objetos para generar la nueva
aplicación.
* Existe un diagrama de clases estándar en la compañía que sirve como guía,
por lo que se pueden cambiar para cubrir las necesidades del proyecto.
* Para los cálculos que se realizan en funciones que se implementaron, se
tiene que llamar al paquete o módulo y ejecutarlas.
* Se puede utilizar una librería para generar el HTML o implementar las
clases para generarlo.
* Se debe validar que los archivos JSON estén correctamente formateados.
## Errores y excepciones a tener presentes
* Transacciones que dejen el monto en negativo
* División por cero.
## Diagrama
![diagramaClases](https://user-images.githubusercontent.com/105433665/178548104-a5fee1f5-fd62-4f90-a4b4-e87245390a8a.png)
