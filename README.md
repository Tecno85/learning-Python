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

---

---

````markdown
## ¿Por qué se inicializa una variable en Python con la palabra `None`?

En Python, una variable se inicializa con la palabra clave `None` cuando deseas declararla pero no asignarle un valor específico de inmediato. Esto es útil por varias razones:

1. **Representar un estado "vacío" o "desconocido"**:  
   `None` es un tipo especial en Python que simboliza la ausencia de un valor. Esto indica claramente que la variable existe pero aún no tiene un valor asignado.
   ```python
   resultado = None  # La variable está definida, pero no tiene valor aún
   ```
````

2. **Evitar errores**:  
   Al inicializar con `None`, reduces el riesgo de errores como intentar usar una variable no definida. Esto es común en lógica condicional o bucles, donde el valor puede ser asignado más adelante.

3. **Mejor legibilidad del código**:  
   Usar `None` deja claro que la variable tendrá un valor asignado en el futuro, lo que mejora la comprensión para otros desarrolladores.

4. **Compatibilidad con comprobaciones explícitas**:  
   Puedes verificar fácilmente si una variable tiene un valor asignado utilizando comparaciones con `None`.
   ```python
   if resultado is None:
       print("La variable aún no tiene un valor asignado.")
   ```

En resumen, `None` es una forma segura y explícita de inicializar una variable cuando su valor se definirá más adelante.

---
---

## Diferencias entre float('-inf') y None

La diferencia entre max_num = float('-inf') y max_num = None radica precisamente en que el primero está inicializado con un valor numérico específico, mientras que el segundo está inicializado con un valor especial que indica "ausencia de valor" en Python.

### Diferencia entre `float('-inf')` y `None`

1. **`float('-inf')`:**

   - Es un valor numérico del tipo `float` que representa el **infinito negativo**.
   - Se puede comparar directamente con números:
     ```python
     max_num = float('-inf')
     print(max_num > 5)  # False
     print(max_num < 5)  # True
     ```
   - Útil cuando trabajas exclusivamente con números y quieres evitar comprobaciones adicionales.  
     Por ejemplo, en un bucle donde siempre comparas valores mayores.

2. **`None`:**
   - Representa "ausencia de valor" o "no definido".
   - No puedes compararlo directamente con números, ya que genera un error:
     ```python
     max_num = None
     print(max_num > 5)  # TypeError
     ```
   - Ideal para casos donde necesitas comprobar si un valor aún no ha sido inicializado:
     ```python
     if max_num is None:
         print("El valor no está asignado aún.")
     ```

### ¿Cuál elegir?

- **`float('-inf')`**:

  - Útil si trabajas únicamente con números.
  - Simplifica comparaciones directas (`numero > max_num` siempre funciona).

- **`None`**:
  - Mejor cuando necesitas manejar valores no definidos o trabajar con múltiples tipos de datos.
  - Ayuda a verificar si un valor se asignó antes de usarlo.

### Conclusión:

`float('-inf')` ya está inicializado con un valor, mientras que `None` indica que el valor no está definido. Elige el que mejor se adapte al contexto de tu problema.

---
