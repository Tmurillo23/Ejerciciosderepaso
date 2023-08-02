def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


num_1 = int(input("Escriba un numero: "))
print(f"El factorial de {num_1} es {factorial(num_1)}")
