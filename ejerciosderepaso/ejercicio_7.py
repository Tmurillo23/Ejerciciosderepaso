lista = [5, 2, 3, 4, 5, 5, 6, 7, 3, 5, 7, 9, 5, 1]
num_max = lista[0]
num_min = lista[0]

for i in range(len(lista)):
    if lista[i] >= num_max:
        num_max = lista[i]
    if lista[i] <= num_min:
        num_min = lista[i]
print(num_max)
print(num_min)