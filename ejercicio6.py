# Ejercicio 6: Suma de dígitos

# Pide al usuario un número y usa un bucle while para calcular la suma de sus
# dígitos.

numero_usuario = int(input("Ingrese un número: "))
suma = 0

while numero_usuario > 0:
    suma += numero_usuario
    numero_usuario -= 1

print(suma)
