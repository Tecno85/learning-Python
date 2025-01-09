# Ejercicio 2: Suma de números positivos

# Crea un programa que permita al usuario introducir números positivos. El
# programa debe sumar esos números y terminar cuando el usuario introduzca un
# número negativo.

suma = 0

while True:
    try:
        numero_usuario = int(input(
            "Ingrese un número positivo para sumar (o negativo para salir): "))
        if numero_usuario < 0:
            break
        suma += numero_usuario
    except ValueError:
        print("Ingresaste un valor diferente a un número")

print(f"La suma de los número positivos es: {suma}")
