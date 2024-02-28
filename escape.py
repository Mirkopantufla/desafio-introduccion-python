import math

radio = float(input('Ingrese el radio en Kilómetros: '))
constanteG = float(input('Ingrese la constante g: '))

resultado = math.sqrt(float(2 * constanteG * (radio * 1000)))

print(f'La velocidad de Escape es: {"{:.1f}".format(resultado)} [m/s]')