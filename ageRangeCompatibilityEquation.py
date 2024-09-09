# Este programa calcula el rango de edad aceptable para relaciones basado en la edad proporcionada por el usuario.
# Si la edad es mayor a 14 años, el rango se calcula mediante la fórmula "mitad de la edad + 7" para la edad mínima
# y "2*(edad - 7)" para la edad máxima.
# Si la edad es 14 o menor, el rango de edad se calcula permitiendo un 10% por encima y por debajo de la edad proporcionada.
# El programa solicita al usuario que ingrese una edad válida entre 1 y 100 y luego muestra el rango correspondiente.

import math
def age_range(age):
    # Calcular el rango de edad según la edad proporcionada
    if age > 14:
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor(2 * (age - 7))
    else:
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    return min_age, max_age

def main():
    # Solicitar al usuario que ingrese la edad
    age = int(input("Ingresa la edad (1 <= n <= 100): "))

    # Verificar que la edad esté dentro del rango válido
    if age < 1 or age > 100:
        print("La edad debe estar entre 1 y 100.")
        return

    # Calcular el rango de edad
    min_age, max_age = age_range(age)

    # Mostrar el resultado incluyendo la edad ingresada
    print(f"Edad ingresada: {age}")
    print(f"Rango de edad: {min_age}-{max_age}")


# Ejecutar la función principal
if __name__ == "__main__":
    main()
