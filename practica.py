"""
Ejercicio 8: Número mayor

Pide al usuario que introduzca números hasta que escriba “0”. Al final,
muestra cuál fue el número más grande que introdujo.
"""

#  Inicializando la variable max_num con la palabra reservado None.
max_num = None

#  Iniciando bucle que permite diferentes opciones.
while True:
    try:
        #  Pidiendo datos por pantalla a usuario.
        numero_usuario = int(input("\nIngrese un número entero o cero (0) para salir: "))

        #  Sale del bucle y manda mensaje cuando no se ingresa ningún dato.
        if numero_usuario == 0:
            if max_num is None:
                print("\nNo ingresaste ningún número entero.\n")
            break

        #  Actualizando el número cuando sea necesario.
        if max_num is None or numero_usuario > max_num:
            max_num = numero_usuario

    except ValueError:
        print("\nValor ingresado inválido, solo números enteros.\n")

# Imprime el número mayor si es necesario.
if max_num is not None:
    print(f"\nEl número mayor es: {max_num}\n")
