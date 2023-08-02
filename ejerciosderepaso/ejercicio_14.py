def media_arimetica(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    media = suma/len(lista)
    return media



lista_1 = [1, 2, 45, 34, 90, 123, 43, 234]
print(f"la media aritmética de las lista: {lista_1} es {media_arimetica(lista_1)}")

