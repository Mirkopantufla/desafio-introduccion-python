pSuscripcion = float(input('Ingrese precio de suscripción: '))
nUsuarios = float(input('Ingrese numero de usuarios: '))
gTotales = float(input('Ingrese los gastos totales: '))
utilidadesAnteriores = float(input('Ingrese las utilidades del año anterior: '))

razon = (pSuscripcion * nUsuarios - gTotales) / utilidadesAnteriores

print(f'Razon entre utilidades actuales y del año anterior: {"{:.2f}".format(razon)}')