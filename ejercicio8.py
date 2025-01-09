"""
Ejercicio 8: Número mayor

Pide al usuario que introduzca números hasta que escriba “0”. Al final,
muestra cuál fue el número más grande que introdujo.
"""
numero_mayor = None  # Inicializo con None el número mayor para empezar

while True:
    try:
        numero_usuario = int(
            input("\nIngrese un número entero positivo, o el (número cero (0) para salir): "))
        
        if numero_usuario == 0:  # Salgo si el usuario ingresa 0
            if numero_usuario is not None:
                print(f"\nEl número mayor es: {numero_mayor}\n")
            else: 
                print("\nNo ingresaste ningún número válido.\n")
            break
        elif numero_usuario < 0:  # Valido que sea positivo
            print("\nEl valor ingresado no corresponde a un número entero positivo.\n")
        else:
            #  Actualizamos el número mayor solo so es más grande
            if numero_mayor is None or numero_usuario > numero_mayor:
                numero_mayor = numero_usuario
    except ValueError: #  Validamos errores en caso de entradas no númericas   
        print("\nDato ingresado es inválido.\n")