# Forma uno usando list slices
print("Palindromos usando list slices")
string_1 = input("Ingrese una palabra: ")
string_1_clean = string_1.replace(" ", "")  # elimino los espacios en blanco del caracter
if string_1_clean == string_1_clean[::-1]:
    print("La palabra es palíndroma")
else:
    print("La palabra no es palíndroma")

print("--------------------------------------------")

# Forma dos usando ciclos:
print("Palindromos usando ciclos")
string_2 = input("Ingrese una palabra: ")
string_2_clean = string_2.replace(" ", "")  # elimino los espacios en blanco del caracter
palindroma = ""
for i in range(len(string_2_clean)):  # Recorro toda el string
    palindroma += string_2_clean[i]  # concateno cada caracter del string para formar uno nuevo
if string_2_clean == palindroma:
    print("La palabra es palíndroma")
else:
    print("La palabra no es palíndroma")
