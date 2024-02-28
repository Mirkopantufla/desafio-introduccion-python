pSuscripcion = float(input('Ingrese precio de suscripción: '))
nUsuarios = float(input('Ingrese numero de usuarios: '))
gTotales = float(input('Ingrese los gastos totales: '))

utilidades = pSuscripcion * nUsuarios - gTotales

print(f'Utilidades: {utilidades}')