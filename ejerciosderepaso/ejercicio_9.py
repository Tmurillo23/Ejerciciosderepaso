import random

matriz = []
filas = int(input("Escriba el numero de filas de la matriz: "))
columnas = int(input("Escriba el numero de columnas de la matriz: "))
for f in range(filas): # Creo una matriz llena de ceros
    ceros = [0] * columnas
    matriz.append(ceros)
for i in range(filas): # Tomo la matriz de ceros y reemplazo cada cero con un número aleatorio
    for j in range(columnas):
        matriz[i][j] = random.randint(0, 10000)

print(matriz)
