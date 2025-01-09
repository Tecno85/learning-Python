""" Ejercicio 7: Menú interactivo

Crea un menú que siga mostrando opciones hasta que el usuario elija “Salir”.
Por ejemplo:
1.	Saludar
2.	Mostrar hora actual
3.	Salir
"""

print("\nMenú Interactivo, escoge una de las opciones: \n"
      "1. Recibir un saludo\n"
      "2. Información de la hora actual\n"
      "3. Salir del Menú\n")

nombre_usuario = str(input("Ingresa tu nombre: "))

while True:
    try:
        print("\nMenú Interactivo, escoge una de las opciones: \n"
              "1. Recibir un saludo\n"
              "2. Información de la hora actual\n"
              "3. Salir del Menú\n")
        opcion_usuario = int(
            input("\nEscoge una de los opciones mencionadas: "))
        if opcion_usuario == 1:
            print(f"Bienvenido a Colombia, {nombre_usuario} es un gusto para "
                  "nosotros que nos visites ")
        elif opcion_usuario == 2:
            print(f"{nombre_usuario}, la hora es: 12:30 pm")
        elif opcion_usuario == 3:
            print(f"Hasta luego, {nombre_usuario} ¡Gracias por usar el Menú")
            break
        else:
            print("Ingresa un valor del 1 al 3: ")
    except ValueError:
        print("Haz ingresado un dato invalido, Ingresa un número del 1 al 3")
