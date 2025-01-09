# Ejercicio 4: Tabla de multiplicar

# Pide al usuario un número y usa un bucle while para imprimir la tabla de
# multiplicar de ese número hasta el 10.

contador = 1
numero_usuario = int(
    input("Ingrese un número para ver su tabla de multiplicar: "))

print(f"Tabla del número {numero_usuario}")
while contador <= 10:
    tabla = numero_usuario * contador
    print(f"{numero_usuario} * {contador} = {tabla}")
    contador += 1
