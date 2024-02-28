pSuscripcion = float(input('Ingrese precio de suscripción: '))
nUsuarios = float(input('Ingrese numero de usuarios normales: '))
nUsuariosPremium = float(input('Ingrese numero de usuarios premium: '))
gTotales = float(input('Ingrese los gastos totales: '))

utilidades = (pSuscripcion * nUsuarios) + (pSuscripcion * 1.5) * nUsuariosPremium - gTotales

print(f'Utilidades: {utilidades}')