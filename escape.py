import math

radio = float(input('Ingrese el radio en Kilómetros (ej: 34): '))
constanteG = float(input('Ingrese la constante g (ej: 8475) '))

resultado = math.sqrt(float(2 * constanteG * (radio * 1000)))

print(f'La velocidad de Escape es: {"{:.1f}".format(resultado)} [m/s]')