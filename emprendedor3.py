pSuscripcion = float(input('Ingrese precio de suscripción (ej: 5000): '))
nUsuarios = float(input('Ingrese numero de usuarios (ej: 5): '))
gTotales = float(input('Ingrese los gastos totales (ej: 2000): '))
utilidadesAnteriores = float(input('Ingrese las utilidades del año anterior (ej: 15000): '))

razon = (pSuscripcion * nUsuarios - gTotales) / utilidadesAnteriores

print(f'Razon entre utilidades actuales y del año anterior: {"{:.2f}".format(razon)}')