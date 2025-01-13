"""
Ejercicio 8: Número mayor

Pide al usuario que introduzca números hasta que escriba “0”. Al final,
muestra cuál fue el número más grande que introdujo.
"""

# Inicialización de la variable max_num
max_num = None

while True:
    try:
        #  Pide al ususario un número
        numero_usuario = int(input("Ingrese un número entero o (cero 0 para salir): "))
        
        #  Si el usuario ingresa cero y no ha ingresado ningún número
        if numero_usuario == 0:
            if max_num is None:
                print("No ingresaste ningún número.")
            break
        
        # Actualizar max_num si es el primero o es mayor al actual
        if max_num is None or numero_usuario > max_num:
            max_num = numero_usuario
    
    #  Muestra mensaje de dato incorrecto, cuando no se ingresa un número
    except ValueError:
        print("Ingresaste un dato incorrecto. Por favor, introduce un número válido.")

#  Muestra el número mayor
if max_num is not None:
    print(f"El número mayor es: {max_num}")


