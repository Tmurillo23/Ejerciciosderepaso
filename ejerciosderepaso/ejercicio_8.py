lista = [1, 2, 2, 3, 5, 5, 8, 9, 10]
lista_inversa = []
for i in range(1, len(lista) + 1):
    lista_inversa.append(lista[-i])
print(lista_inversa)
