# Ejercicio 5: Cuenta regresiva

# Crea un programa que haga una cuenta regresiva desde un número introducido
# por el usuario hasta 0.

numero_usuario = int(input("Introduce un número: "))

while numero_usuario >= 0:
    print(numero_usuario)
    numero_usuario -= 1
    