""" Ejercicio 7: Menú interactivo

Crea un menú que siga mostrando opciones hasta que el usuario elija “Salir”.
Por ejemplo:
1.	Saludar
2.	Mostrar hora actual
3.	Salir
"""

print("\nMenú de Opciones Interactivo\n")
print("1. Saludar")
print("2. Mostrar hora actual")
print("3. Salir")


while True:
    try:
        seleccion_usuario = int(
            input("\nIngresa el número respectivo a la opción que deseas "
                  "realizar: "))
        
        if seleccion_usuario == 1:
            print("\nBienvenido, es un gusto que estes aquí.")
        elif seleccion_usuario == 2:
            print("\nSon las 12:30 pm")
        elif seleccion_usuario == 3:
            print("\nSaliendo del Menú de Opciones Interactivo...\n")
            break
        else:
            print("Ingresa un número del 1 al 3.")

    except ValueError:
        print("Dato inválido, digita un número entero positivo.")
