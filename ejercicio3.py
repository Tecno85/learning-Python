# Ejercicio 3: Adivina el número

# Escribe un programa donde el usuario trate de adivinar un número entre 1 y
# 100. El programa debe seguir pidiendo números hasta que el usuario adivine
# el número correcto. Proporciona pistas como “más alto” o “más bajo”.

numero_secreto = 42

while True:
    try:
        numero_usuario = int(input("Ingrese un número entro 1 y 100: "))
        if numero_usuario == numero_secreto:
            print("Acertaste!")
            break
        elif numero_usuario < numero_secreto:
            print("Ingresa un número más alto")
        else:
            print("Ingresa un número más bajo")
    except ValueError:
        print("Ingrese un número válido")