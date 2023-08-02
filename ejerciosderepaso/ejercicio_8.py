
def lista_inversa(lista):
    lista_inversa = []
    for i in range(1, len(lista) + 1):
        lista_inversa.append(lista[-i])
    return lista_inversa

lista_1 = [1, 2, 2, 3]
print(f"La lista inversa de {lista_1} es {lista_inversa(lista_1)}")
