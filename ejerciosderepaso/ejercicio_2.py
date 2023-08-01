from math import pi


def area_circulo(radio=int(input("Diga el radio del circulo: "))):
    return pi * radio ** 2


area = area_circulo()
print(f"El area del círculo es: {area} unidades cuadradas")
