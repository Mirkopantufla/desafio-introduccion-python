pSuscripcion = float(input('Ingrese precio de suscripción (ej: 5000): '))
nUsuarios = float(input('Ingrese numero de usuarios (ej: 5): '))
gTotales = float(input('Ingrese los gastos totales (ej: 10000): '))

utilidades = pSuscripcion * nUsuarios - gTotales

print(f'Utilidades: {utilidades}')