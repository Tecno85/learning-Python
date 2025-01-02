""" Ejercicio 7: Menú interactivo

Crea un menú que siga mostrando opciones hasta que el usuario elija “Salir”.
Por ejemplo:
1.	Saludar
2.	Mostrar hora actual
3.	Salir
"""
print("\nMenú de opciones interactivo")
while True:
    try:
        print("\n1. Saludo")
        print("2. Mostrar hora actual")
        print("3. Salir")
        opcion_usuario = int(
            input("Ingresa una opción del menú( 1, 2, 3): ")
        )
        if opcion_usuario == 1:
            print("\nHola, cómo estas, es un gusto que estes aquí")
        elif opcion_usuario == 2:
            print("\nLa hora actual son las 12:20 pm")
        elif opcion_usuario == 3:
            print("\nSaliendo del programa...\n")
            break
        else:
            print("\nOpción inválida, por favor ingresa un número entre 1 y 3.\n"
                  )
    except ValueError:
        print("\nDato inválido, ingrese un número entero.\n")
