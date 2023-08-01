def suma_lista(lista_1):
    suma = 0
    for i in range(len(lista_1)):
        suma += lista_1[i]
    return suma


lista = [1, 2, 3, 4, 5, 2, 9]
suma = suma_lista(lista)
print(f"La suma de los valores de la lista: {lista} es: {suma}")
