"""
Ejemplo progresivo de Python (basado en tu código original).
Cada bloque está enumerado y comentado para que puedas estudiar paso a paso.
"""

# ==============================
# [1] Variables y salida básica
# ==============================
# Este bloque crea variables simples (entero y texto) y las imprime.
year = 2026
name = "Diego"
print("[1] Variables iniciales:")
print(f"Año: {year}")
print(f"Nombre: {name}")
print("-" * 40)


# ========================
# [2] Funciones sencillas
# ========================
# Este bloque define una función que recibe parámetros y devuelve un texto.
def build_greeting(user_name: str) -> str:
    return f"Hola, {user_name}!"


print("[2] Función básica:")
print(build_greeting(name))
print("-" * 40)


# ======================================
# [3] Condicionales (if / elif / else)
# ======================================
# Este bloque evalúa condiciones para decidir qué mensaje mostrar.
def describe_year(current_year: int, user_name: str) -> str:
    if current_year > 2025:
        return f"El año {current_year} es mayor que 2025, {user_name}."
    elif current_year == 2025:
        return f"Estamos exactamente en 2025, {user_name}."
    return f"El año {current_year} es menor que 2025, {user_name}."


print("[3] Condicionales:")
print(describe_year(year, name))
print("-" * 40)


# ==========================
# [4] Listas y ciclo for
# ==========================
# Este bloque recorre una lista y muestra cada elemento con su posición.
topics = ["variables", "funciones", "condicionales", "bucles"]
print("[4] Lista + for:")
for index, topic in enumerate(topics, start=1):
    print(f"Tema {index}: {topic}")
print("-" * 40)


# ==========================
# [5] Diccionarios
# ==========================
# Este bloque usa un diccionario para agrupar datos en clave-valor.
student = {
    "nombre": name,
    "año_actual": year,
    "progreso": "inicial",
}

print("[5] Diccionario:")
print(f"Nombre: {student['nombre']}")
print(f"Año actual: {student['año_actual']}")
print(f"Progreso: {student['progreso']}")
print("-" * 40)


# ====================================
# [6] while (repetición con condición)
# ====================================
# Este bloque cuenta de 1 a 3 usando while.
print("[6] while:")
counter = 1
while counter <= 3:
    print(f"Conteo: {counter}")
    counter += 1
print("-" * 40)


# ==================================
# [7] Manejo de errores (try/except)
# ==================================
# Este bloque muestra cómo capturar errores sin detener el programa.
print("[7] try/except:")
value = "10"

try:
    number = int(value)
    result = 100 / number
    print(f"Resultado de 100 / {number} = {result}")
except ValueError:
    print("No se pudo convertir el valor a entero.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
print("-" * 40)


# =====================================
# [8] Punto de entrada del programa
# =====================================
# Este bloque se ejecuta solo cuando corres este archivo directamente.
if __name__ == "__main__":
    print("[8] Fin del ejemplo progresivo de Python.")


# =====================================
# [9] Comprensiones (list/dict/set)
# =====================================
# Este bloque crea colecciones de forma compacta usando comprensiones.
print("[9] Comprensiones:")
numbers = [1, 2, 3, 4, 5, 6]
squares = [number ** 2 for number in numbers]
even_squares = {number: number ** 2 for number in numbers if number % 2 == 0}
unique_letters = {letter for letter in "programacion"}

print(f"Cuadrados: {squares}")
print(f"Cuadrados pares (dict): {even_squares}")
print(f"Letras únicas (set): {sorted(unique_letters)}")
print("-" * 40)


# =====================================
# [10] Funciones lambda y sorted
# =====================================
# Este bloque ordena datos usando una función anónima (lambda).
print("[10] lambda + sorted:")
people = [
    {"name": "Diego", "score": 85},
    {"name": "Ana", "score": 93},
    {"name": "Luis", "score": 78},
]

ranking = sorted(people, key=lambda person: person["score"], reverse=True)
for position, person in enumerate(ranking, start=1):
    print(f"#{position} {person['name']} -> {person['score']}")
print("-" * 40)


# =====================================
# [11] Programación orientada a objetos
# =====================================
# Este bloque define una clase con atributos y métodos.
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def __str__(self) -> str:
        return f"Cuenta(owner={self.owner}, balance={self.balance:.2f})"


print("[11] Clase y objetos:")
account = BankAccount(owner=name, balance=100.0)
account.deposit(50.0)
successful_withdraw = account.withdraw(30.0)
print(account)
print(f"Retiro exitoso: {successful_withdraw}")
print("-" * 40)


# =====================================
# [12] Generadores (yield)
# =====================================
# Este bloque crea un generador para producir valores bajo demanda.
def fibonacci(limit: int):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


print("[12] Generador Fibonacci:")
for value in fibonacci(8):
    print(value, end=" ")
print("\n" + "-" * 40)


# =====================================
# [13] Decoradores
# =====================================
# Este bloque envuelve una función para agregar comportamiento antes y después.
def log_call(function):
    def wrapper(*args, **kwargs):
        print(f"Iniciando: {function.__name__}")
        result = function(*args, **kwargs)
        print(f"Finalizando: {function.__name__}")
        return result

    return wrapper


@log_call
def multiply(x: int, y: int) -> int:
    return x * y


print("[13] Decorador:")
print(f"Resultado multiply(4, 6): {multiply(4, 6)}")
print("-" * 40)


# =====================================
# [14] Context manager (with)
# =====================================
# Este bloque escribe y lee un archivo de forma segura con 'with'.
print("[14] with + archivos:")
file_path = "demo_data.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("Python avanzado\n")
    file.write("Bloques enumerados y comentados\n")

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read().strip()

print(content)
print("-" * 40)


# =====================================
# [15] Manejo de excepciones personalizado
# =====================================
# Este bloque crea una excepción propia para reglas de negocio.
class InvalidAgeError(Exception):
    pass


def validate_age(age: int) -> str:
    if age < 0:
        raise InvalidAgeError("La edad no puede ser negativa.")
    if age < 18:
        return "Menor de edad"
    return "Mayor de edad"


print("[15] Excepción personalizada:")
try:
    print(validate_age(21))
except InvalidAgeError as error:
    print(f"Error: {error}")
print("-" * 40)