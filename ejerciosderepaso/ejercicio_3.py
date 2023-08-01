import random
tamaño = int(input("De que tamaño será la lista: "))
lista = []
for i in range(tamaño):
    lista.append(random.randint(0,100))
print(lista)
