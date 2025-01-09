El bloque `try` y `except` en Python se utiliza para manejar excepciones, que son errores que ocurren durante la ejecución del programa. En este caso, ValueError es una excepción que se lanza cuando una operación recibe un argumento con el tipo correcto pero un valor inapropiado, como intentar convertir una cadena que no representa un número en un entero.


Escribe un programa donde el usuario trate de adivinar un número entre 1 y 100.
El programa debe seguir pidiendo números hasta que el usuario adivine el
número correcto.
Proporciona pistas como “más alto” o “más bajo”.

```py
numero_secreto = 42

while True:
    try:
        numero_usuario = int(input("Ingrese un número entre 1 y 100: "))
        if numero_usuario == numero_secreto:
            print("¡Acertaste!")
            break
        elif numero_usuario < numero_secreto:
            print("Ingresa un número más alto")
        else:
            print("Ingresa un número más bajo")
    except ValueError:
        print("Por favor, ingresa un número válido.")
```

En este código:

El bloque `try` contiene el código que puede lanzar una excepción.
Si el usuario ingresa algo que no puede convertirse en un entero, se lanza una excepción `ValueError`.
El bloque except `ValueError` captura esa excepción y muestra un mensaje de error al usuario, permitiendo que el programa continúe ejecutándose sin fallar.