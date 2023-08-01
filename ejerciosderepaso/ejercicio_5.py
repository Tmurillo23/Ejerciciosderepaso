def fahrenheit_to_celsius(num_1):
    return (num_1 - 32.5) / 1.8


temperatura = fahrenheit_to_celsius(int(input("Diga la temperatura en Fahrenheit: ")))

print(temperatura, "grados Celsius")
