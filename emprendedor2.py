pSuscripcion = float(input('Ingrese precio de suscripción (ej: 5000): '))
nUsuarios = float(input('Ingrese numero de usuarios normales (ej: 5): '))
nUsuariosPremium = float(input('Ingrese numero de usuarios premium (ej: 7): '))
gTotales = float(input('Ingrese los gastos totales (ej: 7000): '))

utilidades = (pSuscripcion * nUsuarios) + (pSuscripcion * 1.5) * nUsuariosPremium - gTotales

print(f'Utilidades: {utilidades}')